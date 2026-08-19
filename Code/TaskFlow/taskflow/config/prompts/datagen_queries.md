# Customer query generation prompt

Generate {n} realistic customer support messages for TaskFlow with intent `{intent}`.

Persona set: {persona_set}          # A for training data, B for test data
Channel mix: 60% email, 40% chat.

Vary deliberately:
- length: one-liners through to three-paragraph complaints
- register: formal, casual, frustrated, confused, terse
- correctness: include typos, missing punctuation, lowercase-only messages
- specificity: some mention exact plan names and amounts, some are vague
- structure: some open with a greeting, some start mid-thought

Never include real personal data. Use obviously fictional names and
@example.com addresses only.

Output one JSON object per line:
{"text": "...", "intent": "{intent}", "channel": "email|chat", "persona": "..."}

Do not restate the intent inside the message text. A message that says "this is a
billing question" teaches the classifier nothing.
