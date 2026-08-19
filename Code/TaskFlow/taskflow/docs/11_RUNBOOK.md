# 11 — Runbook

## First-time setup from a clean clone

```bash
git clone <repo> && cd taskflow
cp .env.example .env            # fill ANTHROPIC_API_KEY and the Gmail paths
uv sync                         # ~2 min
ollama pull qwen2.5:7b-instruct # ~4.7 GB, once
uv run alembic upgrade head
uv run python scripts/generate_kb.py       # or use the committed KB
uv run python scripts/ingest_kb.py --recreate
uv run python -m taskflow.ml.train_classifier
make check                      # should be green
```

First Gmail run opens a browser for OAuth consent and writes `secrets/token.json`.

## Daily

```bash
# terminal 1
make api      # http://localhost:8000  (chat widget at /chat)
# terminal 2
make dash     # http://localhost:8501
```

Ollama must be running (`ollama serve`, or the desktop app). `make preflight` checks it.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| `database is locked` | WAL pragma listener not attached | check `adapters/db/engine.py`; only the API process writes |
| Qdrant returns 0 results | wrong `tenant_id` filter, or an unindexed payload field | create the payload index; log the filter |
| Sparse branch always empty | collection built without `modifier=IDF`, or a different model string at query time | delete `data/qdrant/`, `make ingest` |
| Every draft fails validation | citation markers missing from `response_text` | check the drafting prompt's citation instruction |
| Everything escalates | thresholds too high, or a gate misfiring | `select reason_code, count(*) from traces group by 1` |
| Nothing escalates | gates not wired into `decide()` | run `test_critical_policy_violation_never_auto_sends` |
| Classifier ~0.99 on golden | leakage | `scripts/check_leakage.py`; regenerate the test set with the other provider |
| Gmail 401 | refresh token expired (7-day limit in Testing mode) | delete `secrets/token.json`, re-run, re-consent |
| Ollama very slow | 7B on CPU | switch to `qwen2.5:3b-instruct` in `providers.yaml` |
| Streamlit shows stale data | cached read | `st.cache_data.clear()` or add a TTL |
| Teams alert silent | Workflows webhook URL wrong, or an old O365 connector URL | recreate via Workflows; connector URLs stopped working in May 2026 |

## Reset procedures

```bash
make demo-reset                  # restore the seeded demo database (10 seconds)
rm -rf data/qdrant && make ingest    # rebuild vectors (~2 min)
uv run alembic downgrade base && uv run alembic upgrade head   # nuke the schema
```

## The morning of the demo

1. `make demo-reset`
2. `make preflight` → must exit 0. The Gmail token check is the one that catches you.
3. `make test-e2e` → 5 passed
4. Run through `12_DEMO_SCRIPT.md` once, fully, out loud
5. Confirm the backup recording plays
6. Set `TASKFLOW_LLM_MODE` for your intended path and re-run one scenario to confirm
