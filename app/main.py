"""Finvest AI — Path B shell.

This is your starting point. The chat works: a message you type goes to an
LLM and comes back as plain conversation, and you can switch which user
you're acting as. That's all it does.

It cannot yet answer domain-specific questions, look up records, or take
actions. Building those capabilities is the lab — see coursework.md.

YOUR FIRST TASK: decide what your agent does. Then rename, replace, and
extend everything in here. The comments marked TODO are your entry points.
"""

import json
from pathlib import Path

from fastapi import FastAPI, Header
from fastapi.responses import FileResponse
from pydantic import BaseModel

from . import config
from .services.rag_service import answer_from_docs

app = FastAPI(title="Finvest AI")  # TODO: rename to match your agent

# ---------------------------------------------------------------------------
# Load mock data
# ---------------------------------------------------------------------------
# TODO: Replace with your own data files. These are generic placeholders.
_USERS = {
    u["id"]: u for u in json.loads((config.DATA_DIR / "users.json").read_text())
}

# _RECORDS = json.loads((config.DATA_DIR / "records.json").read_text())


# LLM client - Present in app/llm/model.py
# def _client():
#     """Return an LLM client. Swap this out if you use a different provider."""
#     from openai import AzureOpenAI

#     if not (config.AZURE_ENDPOINT and config.AZURE_API_KEY):
#         raise RuntimeError(
#             "Azure OpenAI credentials are missing. Copy .env.example to .env "
#             "and fill in your values."
#         )
#     return AzureOpenAI(
#         azure_endpoint=config.AZURE_ENDPOINT,
#         api_key=config.AZURE_API_KEY,
#         api_version=config.AZURE_API_VERSION,
#     )


# ---------------------------------------------------------------------------
# Request model
# ---------------------------------------------------------------------------
class ChatRequest(BaseModel):
    message: str


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.get("/api/users")
def users():
    """The users / personas available in the UI switcher."""
    return list(_USERS.values())


@app.post("/api/chat")
def chat(req: ChatRequest, x_user_id: str = Header(default="", alias="X-User-Id")):
    """
    Answers grounded in docs/ via RAG (see app/services/rag_service.py).
    Intent classification, routing, and actions come in Phase 2.
    """
    user = _USERS.get(x_user_id)
    reply = answer_from_docs(req.message, user)
    return {"reply": reply}


@app.get("/")
def index():
    return FileResponse(Path(__file__).parent / "index.html")
