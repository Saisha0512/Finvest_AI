# Chroma persistent client — stores and upserts embedded chunks.

import chromadb
from .. import config

_client = chromadb.PersistentClient(path=str(config.CHROMA_DIR))
collection = _client.get_or_create_collection(config.CHROMA_COLLECTION)


def upsert_chunks(chunks: list[dict], vectors: list[list[float]]):
    collection.upsert(
        ids=[c["id"] for c in chunks],
        embeddings=vectors,
        documents=[c["text"] for c in chunks],
        metadatas=[
            {"heading": c["heading"], "source": c["source"], "category": c["category"]}
            for c in chunks
        ],
    )