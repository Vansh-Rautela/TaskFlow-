"""The compensatory quality scorer.

Unlike safety gates (which veto), quality signals are weighted and compensatory.
This allows a stellar retrieval score to compensate for a slightly weak tone score.
"""

from taskflow.domain.enums import RouteAction
from taskflow.domain.models import ConfidenceBreakdown, GateResult, RoutingDecision


def compute(
    gates: list[GateResult],
    signals: dict[str, float],
    weights: dict[str, float],
    threshold: float,
    draft_confidence: float,
) -> ConfidenceBreakdown:
    """Compute the weighted quality score (Layer 2).
    This computes the score regardless of gate failures, but the decision function
    will prioritize gate failures over the score.
    """
    # Defensive programming: ensure signals map exactly to what's defined in the model
    # Missing signals default to 0.0
    citation_coverage = signals.get("citation_coverage", 0.0)
    grounding_entailment = signals.get("grounding_entailment", 0.0)
    retrieval_relevance = signals.get("retrieval_relevance", 0.0)
    intent_confidence = signals.get("intent_confidence", 0.0)
    tone_alignment = signals.get("tone_alignment", 0.0)

    score = (
        citation_coverage * weights.get("citation_coverage", 0.35)
        + grounding_entailment * weights.get("grounding_entailment", 0.25)
        + retrieval_relevance * weights.get("retrieval_relevance", 0.20)
        + intent_confidence * weights.get("intent_confidence", 0.10)
        + tone_alignment * weights.get("tone_alignment", 0.10)
    )

    return ConfidenceBreakdown(
        gates=gates,
        citation_coverage=citation_coverage,
        grounding_entailment=grounding_entailment,
        retrieval_relevance=retrieval_relevance,
        intent_confidence=intent_confidence,
        tone_alignment=tone_alignment,
        weights=weights,
        score=score,
        threshold=threshold,
        draft_confidence_logged=draft_confidence,
    )


def decide(breakdown: ConfidenceBreakdown) -> RoutingDecision:
    """Make the final routing decision based on ADR-001 (Two-Layer Confidence).
    1. If any gate failed, veto into HUMAN_REVIEW.
    2. Otherwise, if score >= threshold, AUTO_SEND.
    3. Otherwise, escalate to HUMAN_REVIEW due to low_confidence.
    """
    if breakdown.failed_gates:
        # Sort or just take the first failed gate as the primary reason
        primary_failure = breakdown.failed_gates[0]
        return RoutingDecision(
            action=RouteAction.HUMAN_REVIEW,
            reason=primary_failure.reason,
            reason_code=primary_failure.gate_id.value,
            confidence=breakdown,
        )

    if breakdown.score >= breakdown.threshold:
        return RoutingDecision(
            action=RouteAction.AUTO_SEND,
            reason="All gates passed and quality score meets or exceeds threshold",
            reason_code="auto_send",
            confidence=breakdown,
        )

    return RoutingDecision(
        action=RouteAction.HUMAN_REVIEW,
        reason=f"Quality score ({breakdown.score:.3f}) below threshold ({breakdown.threshold:.3f})",
        reason_code="low_confidence",
        confidence=breakdown,
    )
