# Embedding text via Azure - wraps Azure OpenAI embedding calls.
from ..llm.model import get_client
from .. import config


def embed_texts(texts: list[str]) -> list[list[float]]:
    resp = get_client().embeddings.create(
        model=config.AZURE_EMBED_DEPLOYMENT, input=texts
    )
    return [d.embedding for d in resp.data]