# Chunk + store all docs (embedding happens automatically inside Chroma).
# Run whenever docs/ changes: python -m app.rag

from .loader import load_docs
from .splitter import chunk_markdown
from .vectorstore import upsert_chunks


def main():
    all_chunks = []
    for doc in load_docs():
        all_chunks.extend(chunk_markdown(doc))
    print(f"Chunked into {len(all_chunks)} sections.")

    upsert_chunks(all_chunks)
    print(f"Indexed {len(all_chunks)} chunks into Chroma.")


if __name__ == "__main__":
    main()