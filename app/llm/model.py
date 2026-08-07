# Anthropic client factory — single source of truth for the LLM connection.
import os

def get_client():
    import anthropic

    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError(
            "ANTHROPIC_API_KEY is missing. Add it to your .env file."
        )
    return anthropic.Anthropic()