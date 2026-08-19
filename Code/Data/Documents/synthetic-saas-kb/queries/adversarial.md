# Adversarial & Negative Queries

Total: 127 queries


| Query ID | Query / Final Message | Expected Intent | Routing | Ground Truth |
|---|---|---|---|---|
| BILLING-ADV-001 | We want to switch our payment method from a card to a bank transfer. Do you take ACH or wire? | identify which transfer method applies to the customer | answer | KB-BILLING-001 |
| BILLING-ADV-002 | I am not based in the US, so ACH is out for us. Do you still accept PayPal? | confirm PayPal remains an option independent of ACH eligibility | answer | KB-BILLING-001 |
| BILLING-ADV-003 | We added three seats last month and saw a prorated charge. When does the higher seat total start being billed in full? | explain when the full seat count is billed after a mid-cycle add | answer | KB-BILLING-002 |
| BILLING-ADV-004 | My renewal is coming up and last time the payment failed. When exactly will you retry it? | distinguish the renewal date from the dunning retry timing | clarify | KB-BILLING-005 |
| BILLING-ADV-005 | I need the billing statement for last month — is that the invoice or the receipt? I always mix these up. | distinguish an invoice from a receipt | answer | KB-BILLING-003 |
| BILLING-ADV-006 | The invoice from my previous cycle shows a total that is higher than what I remember paying. Can you explain? | reconcile an invoice total against remembered payments | clarify | KB-BILLING-003 |
| BILLING-ADV-007 | We did not pay anything in March, so why is there a receipt for March on our account? | investigate a receipt that appears to contradict a 'no payment' assumption | clarify | KB-BILLING-004 |
| BILLING-ADV-008 | I found a receipt for that charge, but the amount on the receipt does not match my bank statement. | match a receipt to a bank statement line to resolve the discrepancy | clarify | KB-BILLING-004 |
| BILLING-ADV-009 | My card was declined on the renewal, but the charge still shows on my bank statement. You charged me anyway? | resolve the apparent conflict between a declined charge and a statement entry | clarify | KB-BILLING-005 |
| BILLING-ADV-010 | The payment we made three days ago got declined. How many more retries do we get? | explain retry behavior within the dunning grace period | answer | KB-BILLING-005 |
| BILLING-ADV-011 | The other card on our account got declined. Can you switch our subscription back to the first card we used? | identify the correct card before advising a switch | clarify | KB-BILLING-006 |
| BILLING-ADV-012 | I do NOT want to switch to ACH. Is there any other way we can pay without using cards? | list non-card alternatives and confirm availability | clarify | KB-BILLING-001 |
| BILLING-ADV-013 | My card got declined during the verification step. Is that a declined payment, or something else? | distinguish a 3D Secure interruption from an actual declined payment | answer | KB-BILLING-007 |
| BILLING-ADV-014 | I am not in Europe, so I should not have to do this bank verification, right? | correct the assumption that verification applies only in Europe | answer | KB-BILLING-007 |
| BILLING-ADV-015 | We are not in the EU. Do we still need to provide a VAT number? | clarify VAT registration is jurisdiction-dependent, not EU-only | answer | KB-BILLING-008 |
| BILLING-ADV-016 | Last quarter our invoices had no tax, but this month there is a tax line. Why the change? | explain a change in tax treatment across billing periods | clarify | KB-BILLING-008 |
| BILLING-ADV-017 | I changed my billing address but my card was still declined. Are the two related? | connect the billing address to card verification | answer | KB-BILLING-009 |
| BILLING-ADV-018 | On my last invoice the address is still the old one, but I updated it two days ago. Why? | explain that invoices already generated are not re-issued | answer | KB-BILLING-009 |
| BILLING-ADV-019 | How do I connect Salesforce to AcmeFlow? I want our deals to trigger workflows automatically. | misroute | out_of_scope | — |
| BILLING-ADV-020 | One of my workflows stopped mid-execution and will not finish. Can you restart it for me? | misroute | out_of_scope | — |
| BILLING-ADV-021 | Can you add a custom field to our workspace for us? | misroute | out_of_scope | — |
| BILLING-ADV-022 | How do I configure SAML SSO for our organization? | misroute | out_of_scope | — |
| BILLING-ADV-023 | I want to export all our audit logs to our own storage. How do I do that? | misroute | out_of_scope | — |
| BILLING-ADV-024 | We get billed on the 15th of every month. If we add a seat next week, when will the prorated charge appear? | explain when a prorated seat charge shows on the invoice | answer | KB-BILLING-002 |
| CANCEL-ADV-001 | I want to delete my account | cancel_vs_delete_ambiguity | clarify | KB-CANCEL-004 |
| CANCEL-ADV-002 | Can you reactivate my workspace? We cancelled last month. | reactivate_cancelled_workspace | answer | KB-CANCEL-005 |
| CANCEL-ADV-003 | How do I turn off auto-renew on my AcmeFlow plan? | turn_off_auto_renew_maps_to_cancel | answer | KB-CANCEL-001 |
| CANCEL-ADV-004 | Does cancelling delete my workspace and everything in it? | cancellation_does_not_delete | answer | KB-CANCEL-004 |
| CANCEL-ADV-005 | I did NOT cancel my subscription, but you stopped my account and now I can't log in! | investigate_unexpected_access_loss | answer | KB-CANCEL-002 |
| CANCEL-ADV-006 | I never asked you to delete anything, but my data is gone. Did cancelling wipe it out? | cancellation_not_cause_of_data_loss | answer | KB-CANCEL-003 |
| CANCEL-ADV-007 | I cancelled last week. Can I still log in and use AcmeFlow today? | access_continues_until_period_end | answer | KB-CANCEL-002 |
| CANCEL-ADV-008 | Before I deleted my account I thought the data was kept for 60 days. Why can't I get my old workflows back now? | retention_window_already_elapsed | answer | KB-CANCEL-003 |
| CANCEL-ADV-009 | We cancelled on June 2 and you said access runs to July 14, but you cut us off on July 1. | verify_cancellation_access_end_date | answer | KB-CANCEL-002 |
| CANCEL-ADV-010 | That account I told you about earlier - can I cancel it now? | identify_workspace_before_cancelling | clarify | KB-CANCEL-001 |
| CANCEL-ADV-011 | Is the data from the other workspace still being kept? | identify_workspace_for_retention_check | clarify | KB-CANCEL-003 |
| CANCEL-ADV-012 | I want my old plan back at my old price. | clarify_price_lock_eligibility | clarify | KB-CANCEL-005 |
| CANCEL-ADV-013 | I want to keep my data forever but also delete my account. | surface_delete_export_conflict | clarify | KB-CANCEL-004 |
| CANCEL-ADV-014 | We want to come back but only if we keep the exact same price we had three years ago. | price_lock_window_limitation | clarify | KB-CANCEL-005 |
| CANCEL-ADV-015 | How do I add more members to my workspace? | misroute | out_of_scope | — |
| CANCEL-ADV-016 | Your app keeps crashing every time I try to open it | misroute | out_of_scope | — |
| CANCEL-ADV-017 | Can I get a refund for last month's charge? | misroute | out_of_scope | — |
| CANCEL-ADV-018 | What will show up on my bank statement for AcmeFlow charges? | misroute | out_of_scope | — |
| CANCEL-ADV-019 | We're closing down and need to grab everything we can before our 60 days run out. What's the fastest way to save our workflows? | export_within_retention_window | answer | KB-CANCEL-006 |
| ENT-ADV-001 | Do you offer SSO? | Determine whether SSO/SAML is available to the customer. | answer | KB-ENT-001 |
| ENT-ADV-002 | How much does Enterprise cost per user? | Determine Enterprise pricing. | answer | KB-ENT-001 |
| ENT-ADV-003 | Do you guys do volume pricing for big teams? | Determine volume discount availability. | answer | KB-ENT-002 |
| ENT-ADV-004 | We do NOT have an SLA — can we still claim uptime credits? | Determine whether credits apply without a signed SLA. | answer | KB-ENT-004 |
| ENT-ADV-005 | We're not an enterprise account, but we'd really like a dedicated account manager. Is that possible? | Determine DAM availability outside enterprise. | answer | KB-ENT-003 |
| ENT-ADV-006 | You don't support wire transfers for enterprise, do you? | Correct the assumption about wire transfer availability. | answer | KB-ENT-001 |
| ENT-ADV-007 | We had an outage last month — can we get credits for it? | Assess uptime credit eligibility for a vaguely dated outage. | clarify | KB-ENT-004 |
| ENT-ADV-008 | Did our discount change after we added seats back in January? | Determine whether the negotiated discount changed after a seat change. | answer | KB-ENT-002 |
| ENT-ADV-009 | Our contract says we have net terms — what does that mean for when we pay? | Explain net terms and identify the account's specific terms. | clarify | KB-ENT-001 |
| ENT-ADV-010 | That agreement we signed — are we covered for SOC 2 stuff? | Determine whether the referenced agreement covers SOC 2 requests. | clarify | KB-ENT-005 |
| ENT-ADV-011 | We want the standard 30-day refund policy, but our contract says refunds only happen with approval. Which one applies to us? | Reconcile conflicting refund terms. | clarify | KB-ENT-001 |
| ENT-ADV-012 | I see 99.9% in our contract but one of your pages mentions 99.95% somewhere. Which one applies to us? | Reconcile conflicting SLA targets. | clarify | KB-ENT-004 |
| ENT-ADV-013 | How do I set up SCIM? | misroute | out_of_scope | — |
| ENT-ADV-014 | Can you add a feature to your roadmap? | misroute | out_of_scope | — |
| ENT-ADV-015 | I forgot my password — how do I log back in? | misroute | out_of_scope | — |
| ENT-ADV-016 | How do I invite users to our workspace in AcmeFlow? | misroute | out_of_scope | — |
| INVOICE-ADV-001 | Where's my bill for this month? | Determine which billing document the customer means (invoice vs receipt) and which cycle | clarify | KB-INVOICE-001 |
| INVOICE-ADV-002 | Did we get charged for those extra seats we added? | Explain whether added seats produced a charge, referring to the proration line item | answer | KB-INVOICE-001 |
| INVOICE-ADV-003 | What is the GST line on my invoice? Is that an extra fee? | Explain that GST is the tax line item terminology for workspaces billed in India | answer | KB-INVOICE-001 |
| INVOICE-ADV-004 | I didn't receive an invoice email this month. Does that mean we weren't charged? | Explain that a missing notification does not mean there was no charge | answer | KB-INVOICE-004 |
| INVOICE-ADV-005 | My invoice has no tax on it. Does that mean we're tax exempt? | Avoid concluding tax exemption from a single invoice; explain tax depends on jurisdiction and tax status | answer | KB-INVOICE-001 |
| INVOICE-ADV-006 | We don't want our PO number on invoices anymore. Removing it won't change our charges, right? | Confirm removing a PO reference does not change billed amounts | answer | KB-INVOICE-003 |
| INVOICE-ADV-007 | Where can I find last month's invoice? I need it for our accounting team. | Explain that past invoices remain available in the Workspace Billing section | answer | KB-INVOICE-001 |
| INVOICE-ADV-008 | My previous invoice had a credit applied but this month's doesn't. Did we lose the credit? | Explain that credits apply automatically in order of invoice generation and reconcile the credit balance | answer | KB-INVOICE-001 |
| INVOICE-ADV-009 | Can you email that invoice to me? | Resolve which invoice is being referenced and clarify that past invoices are not re-sent | clarify | KB-INVOICE-004 |
| INVOICE-ADV-010 | The other line item on my invoice, what is that for? | Identify which line item the customer is referring to before explaining | clarify | KB-INVOICE-001 |
| INVOICE-ADV-011 | I want our PO number printed on the invoice, but we don't have a PO number yet. Can you still add it? | Surface the conflict: a PO cannot appear on an invoice before a PO number exists | clarify | KB-INVOICE-003 |
| INVOICE-ADV-012 | Our contract says net 30, but can you just charge our card monthly like a normal Pro customer instead? | Surface the conflict between net terms in the signed agreement and automatic card charges | clarify | KB-INVOICE-002 |
| INVOICE-ADV-013 | How do I create a new workflow in my workspace? | misroute | out_of_scope | — |
| INVOICE-ADV-014 | Can you delete my entire workspace and everything in it? | misroute | out_of_scope | — |
| INVOICE-ADV-015 | Which of your integrations connects to our CRM? | misroute | out_of_scope | — |
| INVOICE-ADV-016 | How do I invite more people to our workspace? | misroute | out_of_scope | — |
| PRICING-ADV-001 | I want to upgrade my account | upgrade_intent_ambiguous | clarify | KB-PRICING-006 |
| PRICING-ADV-002 | I cancelled my subscription two weeks ago but I was still charged. I want a refund. | misroute | out_of_scope | — |
| PRICING-ADV-003 | We're on Pro, so we don't have an SLA, right? | sla_availability | answer | KB-PRICING-002 |
| PRICING-ADV-004 | Do I get a dedicated account manager on the Pro plan? | enterprise_account_manager | answer | KB-PRICING-002 |
| PRICING-ADV-005 | Can you add a new integration with our internal tool? | misroute | out_of_scope | — |
| PRICING-ADV-006 | We need to increase our user count from 9 to 20 | seat_increase_ambiguous | clarify | KB-PRICING-003 |
| PRICING-ADV-007 | We removed 3 seats this week but were still billed for 10 - is that a billing error? | seat_removal_billing | answer | KB-PRICING-003 |
| PRICING-ADV-008 | Our monthly Pro renews on the 31st, but last month we were charged on the 30th. Is that a mistake? | monthly_renewal_timing | answer | KB-PRICING-004 |
| PRICING-ADV-009 | We're on annual Pro and want to switch to monthly right away and get a refund for the rest of the year | annual_to_monthly_switch_conflict | clarify | KB-PRICING-004 |
| PRICING-ADV-010 | We're not in the EU, so we don't need to worry about VAT, right? | vat_applicability | answer | KB-PRICING-005 |
| PRICING-ADV-011 | I saw two different prices on our last invoice - which one am I actually paying? | invoice_price_ambiguous | clarify | KB-PRICING-005 |
| PRICING-ADV-012 | We want more executions - can we upgrade just that? | execution_upgrade_ambiguous | clarify | KB-PRICING-006 |
| PRICING-ADV-013 | We switched to annual billing last month. When's the next time we'll be charged? | annual_renewal_timing | answer | KB-PRICING-004 |
| PRICING-ADV-014 | Can I get that trial deal too? | trial_deal_ambiguous | clarify | KB-PRICING-007 |
| PRICING-ADV-015 | I just signed up for the trial but was promised 30 days by our sales rep | trial_duration_conflict | clarify | KB-PRICING-007 |
| PRICING-ADV-016 | How do I export all my workspace data before we cancel? | misroute | out_of_scope | — |
| PRICING-ADV-017 | Is there a discount if we pay in another currency? | currency_discount | answer | KB-PRICING-005 |
| PRICING-ADV-018 | Your API is returning 500 errors for our webhook calls. What's going on? | misroute | out_of_scope | — |
| PRICING-ADV-019 | We're on the free plan so we never get an invoice, right? | free_plan_invoicing | answer | KB-PRICING-001 |
| REFUND-ADV-001 | I want my money back for that charge - will it come back as a refund or as a credit? | distinguish refund to original payment method from a workspace credit balance | answer | KB-REFUND-001 |
| REFUND-ADV-002 | I was NOT charged for anything last month, but I'd still like a refund. | note there is no charge to refund and verify the billing record | answer | KB-REFUND-001 |
| REFUND-ADV-003 | We got charged three days ago and I want my money back. We're still in the window, right? | confirm a charge posted three days ago is within the 30-day window | answer | KB-REFUND-001 |
| REFUND-ADV-004 | Our annual charge was $1,920 and we're 73 days into the term. If a prorated refund were approved, what would we get back? | apply the annual proration formula: 292/365 x $1,920 = $1,536 | answer | KB-REFUND-002 |
| REFUND-ADV-005 | Does removing seats from my plan give me a prorated refund for the unused time? | state that removing seats does not create a prorated refund | answer | KB-REFUND-002 |
| REFUND-ADV-006 | I cancelled my subscription, but I want a full refund for the last six months of charges, plus a goodwill credit, and I need you to approve it today. | identify the conflict and route to exception approval with no guarantee | clarify | KB-REFUND-003 |
| REFUND-ADV-007 | You approved that exception for another customer last week, so approve mine the same way. | clarify that exceptions are case-specific and approval of one does not set precedent | clarify | KB-REFUND-003 |
| REFUND-ADV-008 | I haven't used my credit balance at all yet and I'm cancelling. Will I lose it? | confirm credit balances are forfeited on cancellation unless a contract says otherwise | answer | KB-REFUND-004 |
| REFUND-ADV-009 | Can I move that credit from the refund over to our other workspace? | state that credit balances are not transferable between workspaces | answer | KB-REFUND-004 |
| REFUND-ADV-010 | It's been 10 business days since my PayPal refund was processed and I still don't see the money. | note the refund is past the 5-7 day PayPal estimate and confirm status in the billing record | answer | KB-REFUND-005 |
| REFUND-ADV-011 | How long until the reversal shows up on my bank statement? | map 'reversal' to a refund and provide the timeframe by payment method | answer | KB-REFUND-005 |
| REFUND-ADV-012 | We removed those seats we added earlier in the cycle - will we get a refund for them? | state that no partial refund is created for the unused portion of a prorated seat charge after removal | answer | KB-REFUND-006 |
| REFUND-ADV-013 | I want to downgrade my plan but keep paying the old rate and also get a refund for the downgrade. | flag the conflicting expectations around downgrade pricing and refunds | clarify | KB-REFUND-006 |
| REFUND-ADV-014 | I'd like a partial refund on my subscription. Will that be refunded to my card or given as credit? | distinguish partial-refund eligibility from how the refund is issued | answer | KB-REFUND-006 |
| REFUND-ADV-015 | My automated workflow stopped running halfway through this morning and now my team can't see anything. | misroute | out_of_scope | — |
| REFUND-ADV-016 | Can you integrate AcmeFlow with Salesforce for us? | misroute | out_of_scope | — |
| REFUND-ADV-017 | It would be amazing if you added dark mode to the dashboard. Can you put that on the roadmap? | misroute | out_of_scope | — |
| REFUND-ADV-018 | How do I export all our data before we delete our workspace? | misroute | out_of_scope | — |
| TROUBLE-ADV-001 | I was charged twice for the same month and I want to dispute the second charge. How do I do that? | Investigate a suspected double charge before any dispute is filed | answer | KB-TROUBLE-002 |
| TROUBLE-ADV-002 | Why does my card show two charges this month? I only expected one renewal. | Determine whether the two charges are a duplicate or separate billing events | answer | KB-TROUBLE-002 |
| TROUBLE-ADV-003 | Is it possible I got double charged but in different currencies? My invoice is USD and my statement is in EUR. | Determine whether the EUR statement entry is a conversion of the USD invoice or a separate charge | answer | KB-TROUBLE-003 |
| TROUBLE-ADV-004 | There's an ACMEFLOW charge on my statement that I don't recognize. Why was I charged? | Identify an unrecognized charge by descriptor and matching invoice | answer | KB-TROUBLE-004 |
| TROUBLE-ADV-005 | You did NOT charge me this month, I'm sure of it — but my statement shows a hold from ACMEFLOW. What is that? | Explain that the hold is a pending authorization or pre-authorization, not an actual charge | answer | KB-TROUBLE-002 |
| TROUBLE-ADV-006 | I never got charged anything, so why is there a pending charge for $192 from you sitting on my card? | Explain a pending authorization that has not yet settled | answer | KB-TROUBLE-002 |
| TROUBLE-ADV-007 | Why was last month's renewal $42 higher than this month's? I didn't change anything. | Investigate why a prior renewal was higher than the current one | answer | KB-TROUBLE-001 |
| TROUBLE-ADV-008 | That $192 pending charge from three days ago is still on my card. Will it fall off, or am I getting double charged? | Determine whether a pending entry will settle or be released | answer | KB-TROUBLE-002 |
| TROUBLE-ADV-009 | That charge on my statement — is it even mine? The one I keep telling you about. | Confirm whether a referenced charge belongs to the customer's workspace | answer | KB-TROUBLE-004 |
| TROUBLE-ADV-010 | One of those two entries matches my invoice but the other one doesn't. What is the other one? | Identify an unmapped statement entry and determine whether it is a pending authorization, pre-authorization, or separate charge | answer | KB-TROUBLE-002 |
| TROUBLE-ADV-011 | I didn't buy anything from you but I want a refund for the charge I don't have. Can you process that? | Clarify the contradiction between denying the charge and requesting a refund for it | clarify | KB-TROUBLE-001 |
| TROUBLE-ADV-012 | My workflows are running really slow today and tasks are stuck. Can you help me fix performance? | misroute | out_of_scope | — |
| TROUBLE-ADV-013 | How do I export my reports to PDF? I can't find the button. | misroute | out_of_scope | — |
| TROUBLE-ADV-014 | Your API is returning 500 errors on our webhook calls since yesterday. Is there a known issue? | misroute | out_of_scope | — |
| TROUBLE-ADV-015 | I can't reset my password, the email never arrives. Is there a billing block on my account? | misroute | out_of_scope | — |
