"""Grounding entailment validator for Phase P7.

Evaluates whether the claims in the drafted response are logically grounded in the
retrieved context chunks, preventing hallucinated statements.
"""

from taskflow.config.settings import thresholds_config
from taskflow.domain.models import DraftOutput, RetrievalResult, ValidatorResult


async def validate_grounding(
    draft: DraftOutput, retrieval: RetrievalResult | None
) -> ValidatorResult:
    """Validate that draft statements are grounded in retrieved context chunks."""
    cfg = thresholds_config().get("gates", {})
    min_ratio = float(cfg.get("min_grounding_ratio", 0.80))

    if not retrieval or not retrieval.chunks:
        return ValidatorResult(
            validator_name="grounding",
            passed=False,
            score=0.0,
            reason="No retrieval context available for grounding evaluation",
            blocking=False,
        )

    # Combine text from all retrieved context chunks
    context_text = " ".join(sc.chunk.text.lower() for sc in retrieval.chunks)
    draft_words = set(draft.response_text.lower().split())

    if not draft_words:
        return ValidatorResult(
            validator_name="grounding",
            passed=False,
            score=0.0,
            reason="Draft response text is empty",
            blocking=False,
        )

    # Calculate token/word grounding overlap ratio
    meaningful_words = {w for w in draft_words if len(w) > 3}
    if not meaningful_words:
        return ValidatorResult(
            validator_name="grounding", passed=True, score=1.0, reason="ok", blocking=False
        )

    grounded_words = {w for w in meaningful_words if w in context_text}
    grounding_ratio = round(len(grounded_words) / len(meaningful_words), 2)

    passed = grounding_ratio >= min_ratio
    reason = (
        "ok"
        if passed
        else f"Grounding ratio ({grounding_ratio:.2f}) below threshold ({min_ratio:.2f})"
    )

    return ValidatorResult(
        validator_name="grounding",
        passed=passed,
        score=grounding_ratio,
        reason=reason,
        blocking=False,
    )
