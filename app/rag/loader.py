"""Load markdown knowledge docs from docs/<category>/*.md -- According to the prompt given to the chatbot"""

# This will loop over every subfolder of docs

from .. import config


def load_docs() -> list[dict]:
    docs = []
    for category_dir in sorted(config.DOCS_DIR.iterdir()):
        if not category_dir.is_dir():
            continue
        for path in sorted(category_dir.glob("*.md")):
            docs.append({
                "category": category_dir.name,
                "source": path.stem,
                "text": path.read_text(),
            })
    return docs