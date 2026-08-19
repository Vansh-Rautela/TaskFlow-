# /demo-rehearsal

Full demo dry run. Use in phase P10 and before any real presentation.

1. `make demo-reset`
2. `make preflight` — must exit 0. If any check is red, fix it before continuing.
3. Run all five scenarios and confirm each reason code matches the table in
   `docs/12_DEMO_SCRIPT.md`:
   - `faq_password` -> TEMPLATE_SENT / fastpath_hit / 0 LLM calls
   - `billing_double` -> AUTO_SEND / auto_send
   - `refund_750` -> HUMAN_REVIEW / G1_policy_critical
   - `spam_iphone` -> REJECTED_SPAM / spam_filter / 0 LLM calls
   - `complaint_rant` -> HUMAN_REVIEW / G4_intent / 0 LLM calls
4. Set `TASKFLOW_LLM_MODE=local_only` and re-run all five. Confirm they still pass and
   record the latency difference — this is the offline resilience demo.
5. Stop Ollama, force a Claude failure, and confirm the system degrades to human review
   with `reason_code=all_providers_failed` and an alert is raised.
6. Confirm the trace viewer answers both questions for scenario 2 and scenario 3:
   "why did it send this?" and "why was this escalated?"
7. Report total wall-clock time for the full run and flag any step over 20 seconds.
