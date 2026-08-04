# The one function main.py calls — orchestrates retrieve -> prompt -> answer.

from ..rag.retriever import retrieve
from ..llm.model import get_client
from ..llm.prompts import RAG_SYSTEM_PROMPT
from .. import config


def format_context(chunks: list[dict]) -> str:
    if not chunks:
        return "No relevant policy documents found."
    return "\n\n".join(
        f"[{c['source']} — {c['heading']}]\n{c['text']}" for c in chunks
    )


def answer_from_docs(query: str, user: dict | None) -> str:
    who = f"You are talking to {user['name']}." if user else "You are talking to a user."
    chunks = retrieve(query, k=3)
    context = format_context(chunks)

    client = get_client()
    resp = client.chat.completions.create(
        model=config.AZURE_CHAT_DEPLOYMENT,
        temperature=0.3,
        messages=[
            {"role": "system", "content": RAG_SYSTEM_PROMPT.format(who=who, context=context)},
            {"role": "user", "content": query},
        ],
    )
    return resp.choices[0].message.content