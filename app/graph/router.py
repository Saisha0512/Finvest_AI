# The intent classifier — the agent's 'nervous system'.

INTENTS = [
    "policy_qa",
    "portfolio_balance",
    "watchlist",
    "goals",
    "transactions",
    "off_topic",
]

CLASSIFIER_SYSTEM = f"""You are an intent classifier for Finvest AI, a financial assistant.
Classify the user's message into EXACTLY ONE of these intents. Reply with ONLY
the intent word, nothing else — no punctuation, no explanation.

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

Reply with exactly one word from: {', '.join(INTENTS)}"""


def classify_intent(client, model: str, query: str) -> str:
    resp = client.messages.create(
        model=model,
        max_tokens=10,
        system=CLASSIFIER_SYSTEM,
        messages=[{"role": "user", "content": query}],
    )
    text = resp.content[0].text.strip().lower()
    for intent in INTENTS:
        if intent in text:
            return intent
    return "off_topic"