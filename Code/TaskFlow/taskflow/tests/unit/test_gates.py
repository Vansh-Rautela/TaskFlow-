"""The five tests that encode this project's architecture.

Write these BEFORE implementing services/confidence/. They will fail until P2 is done.
Never delete or weaken them — test_critical_policy_violation_never_auto_sends is the
regression guard for ADR-001 and the centrepiece of the demo.
"""

import pytest

pytest.importorskip("taskflow.services.confidence.gates", reason="implemented in P2")

from taskflow.services.confidence.gates import evaluate_gates
from taskflow.services.confidence.scorer import compute, decide

from taskflow.domain.enums import GateId, Intent, RouteAction, Severity
from taskflow.domain.models import PolicyViolation, ValidatorResult

WEIGHTS = {
    "citation_coverage": 0.35,
    "grounding_entailment": 0.25,
    "retrieval_relevance": 0.20,
    "intent_confidence": 0.10,
    "tone_alignment": 0.10,
}
PERFECT = dict.fromkeys(WEIGHTS, 1.0)


def ok(name: str) -> ValidatorResult:
    return ValidatorResult(validator_name=name, passed=True, score=1.0, reason="ok")


def failed(name: str) -> ValidatorResult:
    return ValidatorResult(
        validator_name=name, passed=False, score=0.0, reason="fail", blocking=True
    )


def errored(name: str) -> ValidatorResult:
    return ValidatorResult(
        validator_name=name,
        passed=False,
        score=0.0,
        reason="validator_error",
        blocking=True,
        errored=True,
    )


def base_kwargs(**overrides):
    kwargs = dict(
        intent=Intent.BILLING,
        intent_confidence=0.99,
        abstain_threshold=0.55,
        validators=[ok("pii_leak"), ok("grounding"), ok("citations")],
        violations=[],
        citations_resolve=True,
        suspicious_context=False,
    )
    kwargs.update(overrides)
    return kwargs


def route(**overrides):
    gates = evaluate_gates(**base_kwargs(**overrides))
    breakdown = compute(
        gates=gates, signals=PERFECT, weights=WEIGHTS, threshold=0.80, draft_confidence=0.99
    )
    return breakdown, decide(breakdown)


def test_critical_policy_violation_never_auto_sends():
    """ADR-001. Every quality signal is perfect. The score clears the threshold.
    It still must not send, because a policy veto is not a weighted term."""
    breakdown, decision = route(
        violations=[
            PolicyViolation(
                rule_id="refund_ceiling",
                severity=Severity.CRITICAL,
                description="exceeds the $500 agent ceiling",
                matched_text="$750",
            )
        ]
    )
    assert breakdown.score > 0.95, "the score really is high — that is the point"
    assert decision.action == RouteAction.HUMAN_REVIEW
    assert decision.reason_code == GateId.G1_POLICY.value


def test_pii_in_draft_blocks_send():
    _, decision = route(validators=[failed("pii_leak"), ok("grounding"), ok("citations")])
    assert decision.action == RouteAction.HUMAN_REVIEW
    assert decision.reason_code == GateId.G2_PII.value


def test_unresolvable_citation_blocks_send():
    _, decision = route(citations_resolve=False)
    assert decision.reason_code == GateId.G3_CITATIONS.value


def test_validator_error_routes_to_human():
    """Fail closed: a crashed or timed-out validator must never be silently skipped."""
    _, decision = route(validators=[ok("pii_leak"), errored("grounding"), ok("citations")])
    assert decision.reason_code == GateId.G6_VALIDATORS.value


def test_classifier_abstention_blocks_send():
    _, decision = route(intent_confidence=0.31)
    assert decision.reason_code == GateId.G5_ABSTAIN.value


def test_clean_draft_auto_sends():
    """The control: with no gate failures and a high score, it does send."""
    _, decision = route()
    assert decision.action == RouteAction.AUTO_SEND
    assert decision.reason_code == "auto_send"
