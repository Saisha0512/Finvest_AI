# Query-time retrieval: Chroma embeds the query and finds top-k chunks.
from .vectorstore import collection

def retrieve(query: str, k: int = 3) -> list[dict]:
    results = collection.query(query_texts=[query], n_results=k)
    return [
        {"text": t, "heading": m["heading"], "source": m["source"]}
        for t, m in zip(results["documents"][0], results["metadatas"][0])
    ]