# Deterministic tone and completeness checks (NOT an LLM call)

This file documents the heuristics implemented in
`services/validate/tone.py` and `services/validate/completeness.py`.
They are deterministic on purpose — see ADR-003. Kept here so the thresholds
are reviewable alongside the prompts.

## Tone (score 0.0-1.0, never blocking)

Start at 1.0 and subtract:
- 0.30 if intent is complaint or refund and no acknowledgement phrase is present
  ("I'm sorry", "I apologise", "I understand your frustration")
- 0.20 if no greeting or no sign-off
- 0.20 if any banned phrase appears: "as an AI", "I'm just a", "unfortunately I cannot
  help", "per my last email"
- 0.15 if more than one exclamation mark
- 0.15 if average sentence length exceeds 30 words
- 0.10 if the response exceeds 350 words

## Completeness (score 0.0-1.0, never blocking)

- Extract question spans from the inbound message (sentences ending in "?" plus
  imperative requests matching "please <verb>", "how do I", "can you", "I need").
- A question is addressed if the response contains a sentence whose embedding cosine
  similarity to the question exceeds 0.45, or which shares a rare content word with it.
- score = addressed / total, 1.0 when there are no extractable questions.
