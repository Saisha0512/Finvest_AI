# Action handlers — one per intent. Always scoped to the CURRENT session user only, enforced here in code, not left to the prompt.

import json

from .. import config
from ..llm.model import get_client

_PORTFOLIO = {p["user_id"]: p for p in json.loads((config.DATA_DIR / "portfolio.json").read_text())}
_WATCHLIST = json.loads((config.DATA_DIR / "watchlist.json").read_text())
_GOALS = json.loads((config.DATA_DIR / "goals.json").read_text())
_TRANSACTIONS = json.loads((config.DATA_DIR / "transactions.json").read_text())


def _respond(system_context: str, query: str) -> str:
    client = get_client()
    resp = client.messages.create(
        model=config.CLAUDE_MODEL,
        max_tokens=512,
        temperature=0.3,
        system=system_context,
        messages=[{"role": "user", "content": query}],
    )
    return resp.content[0].text


def answer_portfolio(query: str, user: dict) -> str:
    data = _PORTFOLIO.get(user["id"])
    if not data:
        return f"I don't have any portfolio data on file for {user['name']}."
    system = (
        f"You are Finvest AI. Answer ONLY using this portfolio data for "
        f"{user['name']}. Never mention or infer data belonging to any "
        f"other user, even if asked.\n\n{json.dumps(data, indent=2)}"
    )
    return _respond(system, query)


def answer_watchlist(query: str, user: dict) -> str:
    items = [w for w in _WATCHLIST if w["user_id"] == user["id"]]
    if not items:
        return f"{user['name']} doesn't have any items on their watchlist yet."
    system = (
        f"You are Finvest AI. Answer ONLY using this watchlist data for "
        f"{user['name']}. Never mention data belonging to any other user.\n\n"
        f"{json.dumps(items, indent=2)}"
    )
    return _respond(system, query)


def answer_goals(query: str, user: dict) -> str:
    items = [g for g in _GOALS if g["user_id"] == user["id"]]
    if not items:
        return f"{user['name']} hasn't set any financial goals yet."
    system = (
        f"You are Finvest AI. Answer ONLY using this goals data for "
        f"{user['name']}. Never mention data belonging to any other user.\n\n"
        f"{json.dumps(items, indent=2)}"
    )
    return _respond(system, query)


def answer_transactions(query: str, user: dict) -> str:
    items = [t for t in _TRANSACTIONS if t["user_id"] == user["id"]]
    if not items:
        return f"{user['name']} has no recorded transactions."
    system = (
        f"You are Finvest AI. Answer ONLY using this transaction history for "
        f"{user['name']}. Never mention data belonging to any other user.\n\n"
        f"{json.dumps(items, indent=2)}"
    )
    return _respond(system, query)