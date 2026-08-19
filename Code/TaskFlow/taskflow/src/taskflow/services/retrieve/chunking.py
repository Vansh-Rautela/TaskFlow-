"""Heading-aware Markdown chunking.

Splits markdown text on section boundaries (##), ensuring chunks remain
coherent. Generates deterministic IDs for idempotent ingestion.
"""

import hashlib
from collections.abc import Iterator
from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentChunk:
    chunk_id: str
    doc_id: str
    title: str
    section_heading: str | None
    text: str
    ordinal: int


def generate_doc_id(relpath: str, title: str) -> str:
    """Generate a deterministic 16-hexdigit document ID."""
    raw = f"{relpath}\n{title}".encode()
    return hashlib.sha256(raw).hexdigest()[:16]


def split_document(
    relpath: str, title: str, markdown_content: str, max_tokens: int = 450, overlap: int = 60
) -> Iterator[DocumentChunk]:
    """Split markdown into roughly `max_tokens` sized chunks, anchored to headings.

    Using a naive word proxy for tokens (1 token ~= 0.75 words, so max_tokens 450 ~= 330 words).
    """
    doc_id = generate_doc_id(relpath, title)

    # Very naive parsing: split by lines, look for headings.
    lines = markdown_content.splitlines()

    current_heading = None
    current_chunk_lines: list[str] = []
    current_word_count = 0

    ordinal = 0
    max_words = int(max_tokens * 0.75)
    overlap_words = int(overlap * 0.75)

    def _yield_chunk(text: str, heading: str | None, ord_num: int) -> DocumentChunk:
        return DocumentChunk(
            chunk_id=f"{doc_id}:{ord_num}",
            doc_id=doc_id,
            title=title,
            section_heading=heading,
            text=text.strip(),
            ordinal=ord_num,
        )

    for line in lines:
        is_heading = line.startswith("#")

        if is_heading:
            header_level = len(line) - len(line.lstrip("#"))
            # If it's a section heading (## or deeper), we might want to start a new chunk
            # if the current chunk is getting large.
            if header_level >= 2 and current_word_count > (max_words // 2) and current_chunk_lines:
                text = "\n".join(current_chunk_lines)
                yield _yield_chunk(text, current_heading, ordinal)
                ordinal += 1

                # Compute overlap (keep last few lines)
                overlap_lines: list[str] = []
                overlap_count = 0
                for prev_line in reversed(current_chunk_lines):
                    words_in_line = len(prev_line.split())
                    if overlap_count + words_in_line > overlap_words:
                        break
                    overlap_lines.insert(0, prev_line)
                    overlap_count += words_in_line

                current_chunk_lines = overlap_lines
                current_word_count = overlap_count

            current_heading = line.lstrip("# ").strip()

        words = line.split()
        current_chunk_lines.append(line)
        current_word_count += len(words)

        # Force split if it gets too large regardless of headings
        if current_word_count >= max_words:
            text = "\n".join(current_chunk_lines)
            yield _yield_chunk(text, current_heading, ordinal)
            ordinal += 1

            overlap_lines = []
            overlap_count = 0
            for prev_line in reversed(current_chunk_lines):
                words_in_line = len(prev_line.split())
                if overlap_count + words_in_line > overlap_words:
                    break
                overlap_lines.insert(0, prev_line)
                overlap_count += words_in_line

            current_chunk_lines = overlap_lines
            current_word_count = overlap_count

    # Yield remaining
    if current_chunk_lines:
        text = "\n".join(current_chunk_lines).strip()
        if text:
            yield _yield_chunk(text, current_heading, ordinal)
