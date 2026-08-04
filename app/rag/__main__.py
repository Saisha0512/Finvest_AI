# Chunk + embed + store all docs. 
# Run whenever docs/ changes: python -m app.rag

from .loader import load_docs
from .splitter import chunk_markdown
from .embeddings import embed_texts
from .vectorstore import upsert_chunks


def main():
    all_chunks = []
    for doc in load_docs():
        all_chunks.extend(chunk_markdown(doc))
    print(f"Chunked into {len(all_chunks)} sections.")

    vectors = embed_texts([c["text"] for c in all_chunks])
    upsert_chunks(all_chunks, vectors)
    print(f"Indexed {len(all_chunks)} chunks into Chroma.")


if __name__ == "__main__":
    main()