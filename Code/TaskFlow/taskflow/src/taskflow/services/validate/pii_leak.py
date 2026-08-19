"""PII & Secret Leakage validator for Phase P7.

Scans outbound LLM drafts for sensitive credit card numbers, SSNs, API secret keys,
and authorization tokens using deterministic regex patterns.
"""

import re

from taskflow.domain.models import DraftOutput, ValidatorResult

CC_PATTERN = re.compile(r"\b(?:\d[ -]*?){13,16}\b")
SSN_PATTERN = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
SECRET_KEY_PATTERN = re.compile(
    r"\b(?:sk|pk)_[a-zA-Z0-9_\-]{16,}\b|Bearer\s+[a-zA-Z0-9._\-]{20,}", re.IGNORECASE
)


async def validate_pii(draft: DraftOutput) -> ValidatorResult:
    """Fail the draft if it contains sensitive PII or API credentials."""
    text = draft.response_text or ""

    if CC_PATTERN.search(text):
        return ValidatorResult(
            validator_name="pii_leak",
            passed=False,
            score=0.0,
            reason="Detected potential PII leak (Credit Card format)",
            blocking=True,
        )

    if SSN_PATTERN.search(text):
        return ValidatorResult(
            validator_name="pii_leak",
            passed=False,
            score=0.0,
            reason="Detected potential PII leak (Social Security Number format)",
            blocking=True,
        )

    if SECRET_KEY_PATTERN.search(text):
        return ValidatorResult(
            validator_name="pii_leak",
            passed=False,
            score=0.0,
            reason="Detected potential API secret or Bearer token leak",
            blocking=True,
        )

    return ValidatorResult(
        validator_name="pii_leak", passed=True, score=1.0, reason="ok", blocking=False
    )
