"""Context injection detector for Phase P5.

Scans retrieved chunk text for prompt injection patterns or untrusted instruction overrides
to set suspicious_context and trigger Gate G7 veto.
"""

import re

from taskflow.domain.models import ScoredChunk

INJECTION_PATTERNS = [
    re.compile(r"ignore (?:all )?(?:previous|prior) (?:instructions|rules|prompts)", re.IGNORECASE),
    re.compile(r"system prompt:", re.IGNORECASE),
    re.compile(r"you are now an? ", re.IGNORECASE),
    re.compile(r"override (?:safety|guardrails|filters|policies)", re.IGNORECASE),
    re.compile(r"\[system_instruction\]", re.IGNORECASE),
]


def detect_context_injection(chunks: list[ScoredChunk]) -> bool:
    """Return True if any retrieved chunk contains suspicious injection patterns."""
    for sc in chunks:
        text = sc.chunk.text
        for pattern in INJECTION_PATTERNS:
            if pattern.search(text):
                return True
    return False
