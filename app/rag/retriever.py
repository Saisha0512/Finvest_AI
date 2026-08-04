# Query-time retrieval: embed the question, find the top-k closest chunks.
from .embeddings import embed_texts
from .vectorstore import collection


def retrieve(query: str, k: int = 3) -> list[dict]:
    query_vector = embed_texts([query])[0]
    results = collection.query(query_embeddings=[query_vector], n_results=k)
    return [
        {"text": t, "heading": m["heading"], "source": m["source"]}
        for t, m in zip(results["documents"][0], results["metadatas"][0])
    ]