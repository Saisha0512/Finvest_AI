# Splitting markdown docs into chunks on ## headers (structure-aware chunking).
import re


def chunk_markdown(doc: dict) -> list[dict]:
    sections = re.split(r"\n(?=## )", doc["text"])
    chunks = []
    for i, section in enumerate(sections):
        section = section.strip()
        if not section:
            continue
        heading = section.split("\n")[0].lstrip("#").strip()
        chunks.append({
            "id": f"{doc['category']}-{doc['source']}-{i}",
            "text": section,
            "heading": heading,
            "source": doc["source"],
            "category": doc["category"],
        })
    return chunks