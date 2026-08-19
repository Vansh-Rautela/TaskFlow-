#!/usr/bin/env python3
"""Knowledge Base ingestion pipeline.

Parses markdown files from data/knowledge_base/, extracts YAML frontmatter,
splits them into overlapping chunks, and stores them in Qdrant with
Dense + Sparse vectors enabled.
"""

import sys
from pathlib import Path

import yaml

from taskflow.adapters.vector.qdrant_store import QdrantVectorStore
from taskflow.services.retrieve.chunking import split_document

KB_DIR = Path("data/knowledge_base")


def parse_markdown_with_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and the remaining markdown content."""
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) >= 3:
        frontmatter_yaml = parts[1]
        body = parts[2].strip()
        try:
            metadata = yaml.safe_load(frontmatter_yaml) or {}
            return metadata, body
        except yaml.YAMLError:
            return {}, content

    return {}, content


def main() -> int:
    if not KB_DIR.exists():
        print(f"Error: {KB_DIR} does not exist. Please ensure data is present.")
        return 1

    print("Initializing Qdrant store and FastEmbed models...")
    store = QdrantVectorStore()

    print("Setting up Qdrant collections and payload indexes...")
    store.setup_collection()

    total_docs = 0
    tenant_id = "taskflow-demo"  # Default tenant

    all_chunks = []

    print(f"Scanning {KB_DIR} for markdown files...")
    for file_path in sorted(KB_DIR.rglob("*.md")):
        relpath = file_path.relative_to(KB_DIR).as_posix()
        content = file_path.read_text(encoding="utf-8")

        metadata, body = parse_markdown_with_frontmatter(content)
        title = metadata.get("title", file_path.stem)

        # Override the deterministic doc_id with the provided one from frontmatter if available
        # so it matches the evaluation sets perfectly.
        official_doc_id = metadata.get("document_id")

        chunks_generator = split_document(relpath, title, body)
        doc_chunks = []

        for c in chunks_generator:
            # We must override the auto-generated doc_id if the frontmatter had one
            # and format the chunk_id properly
            c_doc_id = official_doc_id if official_doc_id else c.doc_id
            c_chunk_id = f"{c_doc_id}:{c.ordinal}"

            # Since DocumentChunk is frozen, we use object.__setattr__ temporarily to override
            # (or we could redefine it if we added replace())
            object.__setattr__(c, "doc_id", c_doc_id)
            object.__setattr__(c, "chunk_id", c_chunk_id)

            all_chunks.append(c)
            doc_chunks.append(c)

        print(f"Parsed {relpath}: {len(doc_chunks)} chunks.")
        total_docs += 1

    print(f"\nDiscovered {total_docs} documents, yielding {len(all_chunks)} chunks.")
    print("Starting vector embedding and ingestion to Qdrant. This may take a minute locally...")

    # Ingest in one go (or could batch if memory is an issue)
    store.ingest(all_chunks, tenant_id=tenant_id)

    print("\nIngestion complete!")
    print(f"Inserted/updated {len(all_chunks)} chunks in collection `{store.collection_name}`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
