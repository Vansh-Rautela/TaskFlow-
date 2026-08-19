---
activation: glob
glob: "tests/**"
---
# Test conventions

- `tests/unit` must run with no network, no Ollama, no Qdrant, in under 10 seconds total.
- Use `FakeLLMProvider` and `FakeVectorStore` from `tests/fixtures/` — never a live model.
- Live Claude calls only in tests marked `@pytest.mark.live`, excluded from `make test`.
- E2E tests assert **routing decisions and reason codes**, never generated prose.
  Model output is not deterministic; decisions are.
- Write the test before the implementation for: gates, confidence scoring, dedupe,
  outbox send-once, SLA computation, circuit breaker transitions.
- Never delete or weaken a failing test to make a build pass. Report it.
