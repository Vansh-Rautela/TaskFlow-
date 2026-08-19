# Tier 3 — Ambiguous Queries (clarification required)

Total: 57 queries


| Query ID | Query / Final Message | Expected Intent | Routing | Ground Truth |
|---|---|---|---|---|
| BILLING-T3-001 | The card option is not working for us and we need another way to pay. What can we do? | clarify which plan, region, and attempted method before recommending an alternative | clarify | KB-BILLING-001 |
| BILLING-T3-002 | We switched plans last week. When does our billing change? | clarify whether the change was an upgrade or downgrade before applying the rule | clarify | KB-BILLING-002 |
| BILLING-T3-003 | I got an invoice notification email but the amount does not look right. Can you check it for me? | clarify which invoice and which amount before investigating | clarify | KB-BILLING-003 |
| BILLING-T3-004 | Hi, I need a receipt for tax purposes. Can you send it to me? | clarify which payment or period the receipt is needed for | clarify | KB-BILLING-004 |
| BILLING-T3-005 | Why was my payment declined? | clarify which charge and which card, and verify the account's dunning state | clarify | KB-BILLING-005 |
| BILLING-T3-006 | I got a 'failed payment' notification but I'm not sure which charge it is about. Can you tell me? | identify the workspace and affected cycle before explaining the dunning stage | clarify | KB-BILLING-005 |
| BILLING-T3-007 | Can you switch my payment method for me? The options in my account are not what I want. | clarify the desired method and eligibility before acting, since updates are self-serve | clarify | KB-BILLING-006 |
| BILLING-T3-008 | I added a card but the charge seems to have disappeared after a verification prompt. Did it fail? | clarify which workspace and charge before checking whether the challenge was completed | clarify | KB-BILLING-007 |
| BILLING-T3-009 | Why are we being charged tax on our AcmeFlow bill? | clarify the billing country, address, and tax registration status before explaining | clarify | KB-BILLING-008 |
| BILLING-T3-010 | How much tax will we pay on our subscription? | clarify jurisdiction details since there is no universal rate | clarify | KB-BILLING-008 |
| BILLING-T3-011 | I updated my billing address but my invoice still shows the old one. What is going on? | clarify which invoice and when the address was updated | clarify | KB-BILLING-009 |
| CANCEL-T3-001 | I'd like to cancel | clarify_cancellation_target | clarify | KB-CANCEL-001 |
| CANCEL-T3-002 | Why can't I cancel my subscription? | clarify_cancellation_obstacle | clarify | KB-CANCEL-001 |
| CANCEL-T3-003 | When will I lose access? | clarify_access_end_date | clarify | KB-CANCEL-002 |
| CANCEL-T3-004 | Is my data still there? | clarify_data_availability | clarify | KB-CANCEL-003 |
| CANCEL-T3-005 | How much longer will our data be kept? | clarify_retention_window_remaining | clarify | KB-CANCEL-003 |
| CANCEL-T3-006 | I want to delete my account | clarify_cancel_vs_delete | clarify | KB-CANCEL-004 |
| CANCEL-T3-007 | Can I get my old price back? | clarify_price_lock_eligibility | clarify | KB-CANCEL-005 |
| CANCEL-T3-008 | Can you export my data for me? | clarify_export_scope | clarify | KB-CANCEL-006 |
| CANCEL-T3-009 | We're thinking of leaving AcmeFlow and want to back up everything before we go | clarify_backup_scope_and_intent | clarify | KB-CANCEL-006 |
| ENT-T3-001 | What are our payment terms? | Retrieve account-specific payment terms from the signed agreement. | clarify | KB-ENT-001 |
| ENT-T3-002 | Can we switch to quarterly billing? | Determine whether a billing cycle change is possible under the agreement. | clarify | KB-ENT-001 |
| ENT-T3-003 | What discount do we get? | Determine the account's negotiated discount from the agreement. | clarify | KB-ENT-002 |
| ENT-T3-004 | Can we talk to our account manager about our contract? | Determine whether the account has an assigned dedicated account manager. | clarify | KB-ENT-003 |
| ENT-T3-005 | Can we get a credit for the outage? | Determine whether an uptime credit applies under the account's SLA. | clarify | KB-ENT-004 |
| ENT-T3-006 | What's our SLA? | Retrieve the account's SLA target and credit terms. | clarify | KB-ENT-004 |
| ENT-T3-007 | Can you send us your security questionnaire? | Determine scope and delivery terms for a security questionnaire request. | clarify | KB-ENT-005 |
| INVOICE-T3-001 | My invoice doesn't add up. Can you check it for me? | Clarify which invoice and which part of it the customer believes is wrong | clarify | KB-INVOICE-001 |
| INVOICE-T3-002 | We need custom invoicing set up for our account. Can you turn that on for us? | Clarify whether the workspace has a signed Enterprise agreement and which custom terms apply | clarify | KB-INVOICE-002 |
| INVOICE-T3-003 | Why is our invoice in the wrong currency? | Clarify which invoice and what currency the customer expected versus the contract currency | clarify | KB-INVOICE-002 |
| INVOICE-T3-004 | My PO number isn't on my invoice. | Clarify which invoice, when the PO was saved, and whether the workspace is Pro or Enterprise | clarify | KB-INVOICE-003 |
| INVOICE-T3-005 | I never got the invoice email. | Clarify which invoice or cycle is expected and verify the current billing contact | clarify | KB-INVOICE-004 |
| INVOICE-T3-006 | There's a charge on my invoice I don't recognize. | Clarify which invoice and which charge the customer does not recognize | clarify | KB-INVOICE-005 |
| INVOICE-T3-007 | I need to dispute something on my bill. | Clarify which invoice and the nature of the dispute | clarify | KB-INVOICE-005 |
| PRICING-T3-001 | What's the price for the Enterprise plan? | enterprise_pricing_query | clarify | KB-PRICING-001 |
| PRICING-T3-002 | What exactly is included in your Enterprise plan? | enterprise_features_query | clarify | KB-PRICING-002 |
| PRICING-T3-003 | How much will my next invoice be after I changed my seats around? | seat_change_invoice_amount | clarify | KB-PRICING-003 |
| PRICING-T3-004 | We want to switch the whole account to annual - how much will we owe right now? | annual_switch_current_cost | clarify | KB-PRICING-004 |
| PRICING-T3-005 | Why does my bank statement show a different amount than my invoice? | statement_invoice_discrepancy | clarify | KB-PRICING-005 |
| PRICING-T3-006 | How much will it cost to upgrade to Pro right now? | upgrade_current_cost | clarify | KB-PRICING-006 |
| PRICING-T3-007 | My trial is ending soon - what will I be charged and when? | trial_conversion_charge | clarify | KB-PRICING-007 |
| PRICING-T3-008 | Can I get a longer trial? | trial_extension | clarify | KB-PRICING-007 |
| PRICING-T3-009 | Is annual billing actually cheaper for us? | annual_savings_comparison | clarify | KB-PRICING-004 |
| REFUND-T3-001 | I'd like to request a refund for a charge on my account. | identify which charge is being refunded before assessing eligibility | clarify | KB-REFUND-001 |
| REFUND-T3-002 | We cancelled our plan - how much of a refund would we get back for the unused time? | clarify that cancellation does not create a prorated refund and ask what policy or agreement applies | clarify | KB-REFUND-002 |
| REFUND-T3-003 | Can you explain the prorated credit line on our last invoice? | identify the specific invoice and prorated amount before explaining the calculation | clarify | KB-REFUND-002 |
| REFUND-T3-004 | I've been a customer for over a year and I'm unhappy. Just make an exception and refund this month's charge. | clarify the specific charge and reason, then explain exceptions require approval and are not automatic | clarify | KB-REFUND-003 |
| REFUND-T3-005 | I see a credit on my workspace. What exactly can I do with it? | identify what the customer wants to do with the credit before explaining application rules | clarify | KB-REFUND-004 |
| REFUND-T3-006 | How long will my refund take? | identify the payment method, amount, and processed date before quoting a timeframe | clarify | KB-REFUND-005 |
| REFUND-T3-007 | I changed my seats around this month. Will I get any money back? | clarify what kind of change was made (added or removed seats, downgrade) before determining eligibility | clarify | KB-REFUND-006 |
| REFUND-T3-008 | Is there any way to get a partial refund for time we won't use? | clarify the specific scenario before assessing whether a partial refund applies | clarify | KB-REFUND-006 |
| TROUBLE-T3-001 | Something is wrong with my bill. Can you fix it? | Clarify which charge and what the customer thinks is wrong before investigating | clarify | KB-TROUBLE-001 |
| TROUBLE-T3-002 | I've been overcharged but I can't tell you how much because I don't have my statement in front of me. I just know the number seemed too big. | Clarify the charge details before any explanation can be given | clarify | KB-TROUBLE-001 |
| TROUBLE-T3-003 | I think I've been double charged but honestly I'm not sure. Can you check? | Clarify the two statement entries before running the duplication check | clarify | KB-TROUBLE-002 |
| TROUBLE-T3-004 | There are some charges on my card I don't understand. I think they might be duplicates but I really can't tell. | Clarify which entries are in question before determining whether duplication exists | clarify | KB-TROUBLE-002 |
| TROUBLE-T3-005 | My bank charge doesn't look right. Can you take a look? | Clarify the statement and invoice amounts before explaining the difference | clarify | KB-TROUBLE-003 |
| TROUBLE-T3-006 | I don't recognize this charge on my card. Is it from you guys? | Clarify the statement entry before confirming whether it is an AcmeFlow charge | clarify | KB-TROUBLE-004 |
