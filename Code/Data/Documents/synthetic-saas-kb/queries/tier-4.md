# Tier 4 — Multi-Turn Threads

Total: 42 queries


| Query ID | Query / Final Message | Expected Intent | Routing | Ground Truth |
|---|---|---|---|---|
| BILLING-T4-001 | So is a wire transfer an option for us, or do we need to talk to our account manager to set that up? | apply Enterprise wire transfer eligibility to a confirmed plan in a multi-turn exchange | answer | KB-BILLING-001 |
| BILLING-T4-002 | So we get billed on the 28th in February and then go back to the 31st in March? | confirm the fallback rule for a renewal day that does not exist in a month | answer | KB-BILLING-002 |
| BILLING-T4-003 | So where exactly is the invoice if it is not attached to the email? | clarify that the email is only a notification and the invoice lives in the workspace | answer | KB-BILLING-003 |
| BILLING-T4-004 | Am I looking in the wrong place, or is the receipt stored somewhere else? | re-explain that the receipt is linked to the payment on the invoice | answer | KB-BILLING-004 |
| BILLING-T4-005 | What actually happens to our account if we ignore it past day 7? | explain past-due and restriction/suspension consequences of not acting | answer | KB-BILLING-005 |
| BILLING-T4-006 | So what happens to the charge that failed? Will they try the new card automatically? | confirm pending retries are attempted against the valid method on file | answer | KB-BILLING-006 |
| BILLING-T4-007 | If it still did not go through after I approved it, what happens next? | explain the dunning path if the payment did not post after the challenge | answer | KB-BILLING-007 |
| BILLING-T4-008 | Then how do I know what percentage was applied on my invoice? | explain the GST line reflects the applicable jurisdiction's rate and where to see it | answer | KB-BILLING-008 |
| BILLING-T4-009 | Changing the address will not automatically change who gets the invoice emails, correct? | confirm billing address and billing contact are separate | answer | KB-BILLING-009 |
| CANCEL-T4-001 | did my cancellation actually go through? | confirm_cancellation_confirmation | answer | KB-CANCEL-001 |
| CANCEL-T4-002 | so access stops on the 15th? | confirm_access_end_date | answer | KB-CANCEL-002 |
| CANCEL-T4-003 | so is our data still around? | confirm_data_within_retention_window | answer | KB-CANCEL-003 |
| CANCEL-T4-004 | should we go ahead and delete now? | confirm_delete_after_export | answer | KB-CANCEL-004 |
| CANCEL-T4-005 | so we'd still get our old price? | confirm_price_lock_applies | answer | KB-CANCEL-005 |
| CANCEL-T4-006 | is the data gone for good? | confirm_data_loss_after_delete_without_export | answer | KB-CANCEL-006 |
| ENT-T4-001 | If we're on quarterly billing, is one purchase order enough for all four invoices this year? | Determine whether one PO covers the whole year or a new PO is needed per billing cycle. | answer | KB-ENT-001 |
| ENT-T4-002 | So after we go to 260 seats, does the 5% still hold, or does the 10% kick in? | Determine which discount tier applies after a seat increase under the agreement. | answer | KB-ENT-002 |
| ENT-T4-003 | So I should loop Dana in on the seat forecast before we talk to billing, right? | Confirm DAM coordination for seat and renewal planning. | answer | KB-ENT-003 |
| ENT-T4-004 | Does 45 minutes on a single day actually put us under for the month? | Determine whether the reported downtime breaches the monthly uptime target under the agreement. | answer | KB-ENT-004 |
| ENT-T4-005 | So the NDA needs to be in place before they send the report? | Confirm that confidentiality and non-disclosure terms govern delivery of SOC 2 documentation. | answer | KB-ENT-005 |
| INVOICE-T4-001 | So the $32 line is really just the two seats we added on the 12th, right? Nothing else on there? | Confirm the prorated seat addition accounts for the $32 difference | answer | KB-INVOICE-001 |
| INVOICE-T4-002 | So with our agreement, this invoice should print PO-88213 and be due 30 days from the invoice date, correct? | Confirm PO and net-30 terms from the signed Enterprise agreement | answer | KB-INVOICE-002 |
| INVOICE-T4-003 | So our next invoice will show that PO, but the current one that was already generated won't, right? | Confirm the PO appears only on invoices generated after it was saved | answer | KB-INVOICE-003 |
| INVOICE-T4-004 | If we update it now, the next invoice notification goes to the new address? | Confirm the updated billing contact receives the next notification | answer | KB-INVOICE-004 |
| INVOICE-T4-005 | So those aren't duplicate charges — the second invoice is just the next month's cycle, right? | Confirm the two invoices are separate billing cycles, not a duplicate charge | answer | KB-INVOICE-005 |
| PRICING-T4-001 | Does the middle one come with audit logs? | pro_audit_logs | answer | KB-PRICING-001 |
| PRICING-T4-002 | Yeah, does that one include the reporting? | pro_analytics_availability | answer | KB-PRICING-002 |
| PRICING-T4-003 | So will we get money back for the people we removed? | seat_removal_refund | answer | KB-PRICING-003 |
| PRICING-T4-004 | If we switch back to monthly, do we lose the money we already paid? | annual_to_monthly_switch_refund | answer | KB-PRICING-004 |
| PRICING-T4-005 | So should the amount change now that we switched to EUR? | currency_switch_conversion | answer | KB-PRICING-005 |
| PRICING-T4-006 | When would the switch back to Free kick in? | downgrade_effective_date | answer | KB-PRICING-006 |
| PRICING-T4-007 | So what's the first charge going to be on the 17th? | trial_conversion_charge | answer | KB-PRICING-007 |
| REFUND-T4-001 | But we were charged two weeks ago - does that charge still count for a refund? | confirm a separate charge posted within the last 30 days remains eligible even after cancellation | answer | KB-REFUND-001 |
| REFUND-T4-002 | So how much are we getting back? | apply the prorated refund formula: 15/30 x $120 = $60 | answer | KB-REFUND-002 |
| REFUND-T4-003 | Who actually decides whether it gets approved? | explain exceptions are approved by the appropriate approver, typically a Billing Operations manager | answer | KB-REFUND-003 |
| REFUND-T4-004 | how much will we actually end up paying? | apply the credit to the invoice: $192 - $120 = $72 due | answer | KB-REFUND-004 |
| REFUND-T4-005 | Is something wrong with it? | confirm the refund is still within the estimate window and nothing is necessarily wrong | answer | KB-REFUND-005 |
| REFUND-T4-006 | we shouldn't expect any credit for the rest of March, right? | confirm no partial refund or credit for unused seat time after a downgrade | answer | KB-REFUND-006 |
| TROUBLE-T4-001 | So there are two line items on it and one says the amount is from an overdue period. Does that mean I'm being double billed for last month? | Explain that the overdue-period line item is the outstanding balance from a failed cycle collected at renewal, not a duplicate charge | answer | KB-TROUBLE-001 |
| TROUBLE-T4-002 | I checked my statement again and both are marked settled. Does that mean it's a double charge for sure? | Verify whether two settled charges cover the same invoice or period before confirming duplication | answer | KB-TROUBLE-002 |
| TROUBLE-T4-003 | So is that difference just the currency conversion, or did you actually overcharge me? | Confirm the statement amount is a market-rate conversion of the USD invoice, not an overcharge | answer | KB-TROUBLE-003 |
| TROUBLE-T4-004 | I searched for 'AcmeFlow Inc.' on the statement and it's not there. Is this charge really from you? | Explain that ACMEFLOW is the processor descriptor while AcmeFlow Inc. is the legal entity, and confirm the charge against the matching invoice | answer | KB-TROUBLE-004 |
