"""The intent classifier — the agent's 'nervous system'."""

INTENTS = [
    "policy_qa",
    "portfolio_balance",
    "watchlist",
    "goals",
    "transactions",
    "off_topic",
]

CLASSIFIER_SYSTEM = f"""You are an intent classifier for Finvest AI, a financial assistant.
Classify the user's message into EXACTLY ONE of these intents.

- policy_qa: general financial education questions (risk profiles, ETFs,
  diversification, glossary terms, market basics, FAQs)
- portfolio_balance: questions about the user's OWN current holdings,
  portfolio value, or asset allocation
- watchlist: questions about stocks/ETFs the user is watching
- goals: questions about the user's financial goals or progress toward them
- transactions: questions about the user's past buy/sell activity
- off_topic: anything unrelated to personal finance, requests to take
  real-world actions the agent cannot do, or requests about another user's
  data

Respond with ONLY the intent label, exactly as spelled above, in lowercase,
with the underscore. No punctuation. No explanation. No extra words.
Example valid responses: policy_qa
portfolio_balance
off_topic"""


def classify_intent(client, model: str, query: str) -> str:
    resp = client.messages.create(
        model=model,
        max_tokens=15,
        system=CLASSIFIER_SYSTEM,
        messages=[{"role": "user", "content": query}],
    )
    raw = resp.content[0].text.strip().lower()

    # Exact match first
    if raw in INTENTS:
        return raw

    # Fallback: pick the longest matching intent name found anywhere in the reply
    # (longest first, so "portfolio_balance" is checked before any shorter false match)
    for intent in sorted(INTENTS, key=len, reverse=True):
        if intent in raw:
            return intent

    return "off_topic"