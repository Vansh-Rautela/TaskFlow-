"""Domain error types.

Adapters translate vendor SDK exceptions into these so that services never import
an SDK and never branch on a vendor-specific exception type.
"""


class TaskFlowError(Exception):
    """Base for every error this application raises deliberately."""


class ConfigError(TaskFlowError):
    """Missing or invalid configuration. Raised at startup, never at request time."""


class TransientError(TaskFlowError):
    """Worth retrying: timeouts, 5xx, connection resets."""


class ProviderError(TransientError):
    """An LLM provider failed in a way that should trigger failover."""


class SchemaError(ProviderError):
    """The model produced output that does not satisfy the schema.

    With constrained decoding this should only happen on a refusal stop reason or a
    max_tokens truncation. Both mean: try the next provider.
    """


class AllProvidersFailed(TaskFlowError):
    """Every configured provider failed. The message routes to human review."""


class RetrievalUnavailable(TransientError):
    """The vector store could not be reached. Fast path still works; everything else escalates."""


class ConflictError(TaskFlowError):
    """Optimistic lock lost — someone else actioned this review first."""


class DuplicateMessage(TaskFlowError):
    """This dedupe_key has already been processed. Not an error condition; a signal."""
