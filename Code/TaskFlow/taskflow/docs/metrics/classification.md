# Intent Classification Metrics — Phase P6

- **Samples Evaluated:** 14
- **Overall Accuracy:** 42.86%
- **Macro F1 Score:** 0.2708
- **Average Latency:** 0.3 ms

## Per-Intent Breakdown

| Intent | Precision | Recall | F1 Score | Support |
|---|---|---|---|---|
| billing | 1.00 | 1.00 | 1.00 | 2 |
| cancellation | 0.00 | 0.00 | 0.00 | 2 |
| complaint | 0.00 | 0.00 | 0.00 | 2 |
| enterprise | 0.00 | 0.00 | 0.00 | 2 |
| other | 0.00 | 0.00 | 0.00 | 2 |
| refund | 0.50 | 1.00 | 0.67 | 2 |
| technical | 0.33 | 1.00 | 0.50 | 2 |
| unknown | 0.00 | 0.00 | 0.00 | 0 |

## Evaluation Configuration
- **Model Classifier:** `ProviderRouter` Structured Output
- **Fallback:** Deterministic Keyword Classifier
- **Dataset:** `data/datasets/classifier_test.jsonl`
