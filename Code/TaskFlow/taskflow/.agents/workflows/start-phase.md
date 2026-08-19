# /start-phase

Begin a new phase from the implementation plan.

1. Read `docs/03_IMPLEMENTATION_PLAN.md` and identify the lowest-numbered phase whose
   Definition of done is not fully ticked.
2. Read that phase's Prerequisites and confirm each one is actually satisfied in the
   repository — do not trust the checkbox alone; verify the file or test exists.
3. Read `docs/04_SCHEMAS.md` for every object the phase touches.
4. Read any `docs/` file the phase names in its Reading list.
5. Produce a plan containing:
   - the exact files you will create or modify
   - the interfaces (function and class signatures) you will add
   - the tests you will write, and which of them you will write *before* the code
   - anything in the phase description that is ambiguous, with your proposed reading
6. **Stop. Present the plan and wait for approval. Do not write code in this step.**
7. After approval, implement one numbered implementation step at a time, running
   `make test` between steps.
