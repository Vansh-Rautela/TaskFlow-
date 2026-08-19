---
activation: glob
glob: "src/taskflow/adapters/**"
---
# Adapters are the only place SDKs live

This layer implements a Protocol from `taskflow.ports` and nothing else. Rules:

- Every outbound network call is wrapped in `@circuit_breaker` with a named breaker and a
  fallback documented in `docs/09_FAILURE_MODES.md`.
- Never catch bare `Exception`. Translate SDK errors into `taskflow.domain.errors` types
  so services stay SDK-agnostic.
- Model names, base URLs and timeouts come from `config/providers.yaml` via settings —
  never as literals in this code.
- Every adapter has an integration test marked `@pytest.mark.integration`.
- LLM adapters must handle the two structured-output failure cases explicitly:
  a refusal stop reason and a max_tokens stop reason both raise `SchemaError`, which
  triggers fallback to the next provider.
