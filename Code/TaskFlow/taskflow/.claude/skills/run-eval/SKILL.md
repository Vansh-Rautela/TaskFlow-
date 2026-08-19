---
name: run-eval
description: Runs the retrieval and classifier evaluations and updates the published metrics. Use after changing chunking, retrieval parameters, datasets, or the classifier.
---
# Run the evaluation suite

1. `python scripts/check_leakage.py` — must exit 0 before any metric is trusted.
   If it fails, stop: the datasets overlap and every number after this is meaningless.
2. `python scripts/eval_retrieval.py` — writes `docs/metrics/retrieval.md`.
   Report recall@5, MRR@10, gap-rate, and the hybrid-vs-dense-only delta.
3. `python -m taskflow.ml.evaluate` — writes `docs/metrics/classifier.md`.
   Report accuracy, macro-F1, per-class precision/recall, abstain rate, and the confusion
   matrix, **for both the synthetic test set and the hand-written golden set**.
4. State the gap between the two sets explicitly. The gap is the finding, not an
   embarrassment — `docs/07_EVAL_METHODOLOGY.md` explains why.
5. Compare against `src/taskflow/ml/artifacts/expected_metrics.json`. If macro-F1 on the
   golden set dropped by more than 0.03, or complaint recall fell below 0.85, report a
   regression and do not update the expected metrics file.
6. If metrics improved and are stable, update `expected_metrics.json` in the same commit
   as the change that caused the improvement.

Never report a single headline accuracy number without the golden-set number beside it.
