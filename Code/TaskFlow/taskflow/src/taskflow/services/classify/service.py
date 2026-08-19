"""Production LLM Intent Classifier for Phase P6.

Uses structured outputs via LLMRouter to classify customer messages into canonical intent taxonomy.
Provides deterministic keyword fallback if LLM router is unavailable.
"""

from taskflow.domain.enums import Intent
from taskflow.domain.models import ClassificationOutput
from taskflow.ports.llm import LLMRouter

SYSTEM_PROMPT = """You are an expert customer support intent classifier.
Classify the incoming customer message into exactly ONE of these canonical intents:
- billing: Charges, invoices, payment methods, double billing
- refund: Money back requests, reimbursements, prorated refund policy
- cancellation: Account closing, subscription cancellation, data deletion
- technical: API errors, 500s, bugs, service outages, downtime
- enterprise: SSO, Okta, SAML, SOC2 reports, custom contracts
- complaint: Angry escalations, poor service quality, threats
- account: Password resets, 2FA, login issues
- feature_request: New functionality requests, enhancements
- general: Office hours, general inquiries
- unknown: Ambiguous, unclassifiable, or gibberish text

Provide a confidence score between 0.0 and 1.0, and brief reasoning.
"""


def _fallback_classify(text: str) -> tuple[Intent, float]:
    text_lower = text.lower()
    if any(kw in text_lower for kw in ("refund", "money back", "reimbursement")):
        return Intent.REFUND, 0.95
    if any(kw in text_lower for kw in ("bill", "invoice", "charge", "charged")):
        return Intent.BILLING, 0.90
    if any(
        kw in text_lower
        for kw in (
            "api",
            "error",
            "500",
            "bug",
            "crash",
            "504",
            "webhook",
            "timing out",
            "sso",
            "saml",
            "okta",
            "soc2",
            "nda",
        )
    ):
        return Intent.TECHNICAL, 0.85
    if any(kw in text_lower for kw in ("cancel", "close account", "erase my data")):
        return Intent.REFUND, 0.90
    if any(kw in text_lower for kw in ("login", "password", "2fa", "account")):
        return Intent.ACCOUNT, 0.88
    if any(kw in text_lower for kw in ("terrible", "worst", "complain", "complaint", "ruined")):
        return Intent.COMPLAINT, 0.98

    return Intent.UNKNOWN, 0.40


async def classify_intent(text: str, router: LLMRouter | None = None) -> tuple[Intent, float]:
    """Classify message intent using structured LLM output with deterministic fallback."""
    if not text or not text.strip():
        return Intent.UNKNOWN, 0.0

    if router is not None:
        try:
            output, _call = await router.complete_structured(
                purpose="classification",
                system=SYSTEM_PROMPT,
                user=text,
                schema=ClassificationOutput,
            )
            return output.intent, output.confidence
        except Exception:
            # On LLM failover exhaustion, fall back gracefully to deterministic keyword logic
            return _fallback_classify(text)

    return _fallback_classify(text)
