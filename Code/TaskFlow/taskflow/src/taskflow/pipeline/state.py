"""The state object passed down the pipeline.

Must be frozen. Stages mutate by creating a new copy via replace().
This eliminates an entire class of 'who mutated my state' bugs.
"""

from collections.abc import Mapping
from dataclasses import dataclass

from taskflow.domain.enums import Intent
from taskflow.domain.models import (
    ConfidenceBreakdown,
    DraftOutput,
    InboundMessage,
    RetrievalResult,
    RoutingDecision,
    Trace,
    ValidatorResult,
)


@dataclass(frozen=True)
class PipelineState:
    message: InboundMessage
    trace: Trace
    intent: Intent | None = None
    intent_confidence: float = 0.0
    retrieval: RetrievalResult | None = None
    draft: DraftOutput | None = None
    validators: tuple[ValidatorResult, ...] = ()
    confidence: ConfidenceBreakdown | None = None
    decision: RoutingDecision | None = None

    # Store dynamic threshold configurations mapped per intent
    thresholds: Mapping[str, float] | None = None  # Expected to be populated inside pipeline

    def replace(self, **kwargs) -> "PipelineState":
        from dataclasses import replace

        return replace(self, **kwargs)
