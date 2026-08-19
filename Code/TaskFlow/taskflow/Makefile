.DEFAULT_GOAL := help
PY := uv run

help:  ## show all targets
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "};{printf "  \033[36m%-14s\033[0m %s\n",$$1,$$2}'

# ---------- run (two commands, no docker, no servers) ----------
api:           ## FastAPI + worker + SLA + pollers, all in one process :8000
	$(PY) uvicorn taskflow.api.main:app --reload --port 8000
dash:          ## Streamlit review queue + trace viewer :8501
	$(PY) streamlit run src/taskflow/dashboard/app.py --server.port 8501

# ---------- quality ----------
lint:          ## format + autofix
	$(PY) ruff format src tests scripts && $(PY) ruff check --fix src tests scripts
typecheck:     ## mypy + architectural import boundaries
	$(PY) mypy src && $(PY) lint-imports
test:          ## unit tests (fast, no network, no disk services)
	$(PY) pytest tests/unit -q
test-int:      ## integration tests (qdrant on disk, ollama running)
	$(PY) pytest -m integration -q
test-e2e:      ## the five demo scenarios
	$(PY) pytest tests/e2e -q
check: lint typecheck test  ## everything fast — run before every commit

# ---------- data + models ----------
migrate:       ## apply database migrations
	$(PY) alembic upgrade head
kb:            ## generate the 42-document knowledge base
	$(PY) python scripts/generate_kb.py
datasets:      ## generate classifier train/test + check leakage
	$(PY) python scripts/generate_datasets.py && $(PY) python scripts/check_leakage.py
ingest:        ## (re)build the embedded Qdrant collection
	$(PY) python scripts/ingest_kb.py --recreate
train:         ## train the intent classifier and publish metrics
	$(PY) python -m taskflow.ml.train_classifier && $(PY) python -m taskflow.ml.evaluate
eval:          ## retrieval + classifier evaluation reports
	$(PY) python scripts/eval_retrieval.py && $(PY) python -m taskflow.ml.evaluate

# ---------- demo ----------
scenario:      ## run one scenario: make scenario S=refund_750
	$(PY) python scripts/run_scenario.py --scenario $(S)
preflight:     ## demo readiness check — must exit 0
	$(PY) python scripts/preflight.py
demo-reset:    ## restore the seeded demo database
	cp data/snapshots/demo_seed.db data/taskflow.db && echo "demo db restored"
local:         ## force the offline path (no cloud LLM at all)
	TASKFLOW_LLM_MODE=local_only $(PY) python scripts/run_scenario.py --all

setup:         ## first-time setup
	uv sync && $(PY) alembic upgrade head && ollama pull qwen2.5:7b-instruct
