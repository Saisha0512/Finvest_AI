# One node per graph step.
from .. import config
from ..llm.model import get_client
from ..services.rag_service import answer_from_docs
from ..services import finance_service
from .router import classify_intent


def classify_node(state: dict) -> dict:
    client = get_client()
    intent = classify_intent(client, config.CLAUDE_MODEL, state["query"])
    return {"intent": intent}


def policy_node(state: dict) -> dict:
    return {"reply": answer_from_docs(state["query"], state["user"])}


def portfolio_node(state: dict) -> dict:
    return {"reply": finance_service.answer_portfolio(state["query"], state["user"])}


def watchlist_node(state: dict) -> dict:
    return {"reply": finance_service.answer_watchlist(state["query"], state["user"])}


def goals_node(state: dict) -> dict:
    return {"reply": finance_service.answer_goals(state["query"], state["user"])}


def transactions_node(state: dict) -> dict:
    return {"reply": finance_service.answer_transactions(state["query"], state["user"])}


def off_topic_node(state: dict) -> dict:
    return {
        "reply": (
            "I'm Finvest AI — I can help with your portfolio, watchlist, "
            "financial goals, transaction history, and general investing "
            "questions. I can't help with that request."
        )
    }