"""Inbound Message Preprocessing Service.

Redacts sensitive PII (credit card numbers, SSNs, API keys) from inbound message text
before passing to LLMs, ensuring raw sensitive credentials never enter prompt context.
"""

import re

CC_PATTERN = re.compile(r"\b(?:\d[ -]*?){13,16}\b")
SSN_PATTERN = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
SECRET_KEY_PATTERN = re.compile(
    r"\b(?:sk|pk)_[a-zA-Z0-9_\-]{16,}\b|Bearer\s+[a-zA-Z0-9._\-]{20,}", re.IGNORECASE
)


def preprocess_message_text(text: str) -> str:
    """Return PII-redacted text safe for LLM prompt context."""
    if not text:
        return ""

    redacted = CC_PATTERN.sub("[REDACTED_CREDIT_CARD]", text)
    redacted = SSN_PATTERN.sub("[REDACTED_SSN]", redacted)
    redacted = SECRET_KEY_PATTERN.sub("[REDACTED_API_KEY]", redacted)
    return redacted
