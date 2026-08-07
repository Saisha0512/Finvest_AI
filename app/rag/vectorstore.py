# Chroma persistent client with a local sentence-transformer embedding function — no external API calls for embeddings

import chromadb
from chromadb.utils import embedding_functions
from .. import config

_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=config.EMBEDDING_MODEL_NAME
)

_client = chromadb.PersistentClient(path=str(config.CHROMA_DIR))
collection = _client.get_or_create_collection(
    config.CHROMA_COLLECTION,
    embedding_function=_ef,
    metadata={"hnsw:space": "cosine"},
)


def upsert_chunks(chunks: list[dict]):
    """Chroma embeds these automatically using the collection's embedding_function."""
    collection.upsert(
        ids=[c["id"] for c in chunks],
        documents=[c["text"] for c in chunks],
        metadatas=[
            {"heading": c["heading"], "source": c["source"], "category": c["category"]}
            for c in chunks
        ],
    )