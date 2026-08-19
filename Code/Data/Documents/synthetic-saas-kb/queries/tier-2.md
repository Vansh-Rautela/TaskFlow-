# Tier 2 — Conditional / Policy-Boundary Queries

Total: 126 queries


| Query ID | Query / Final Message | Expected Intent | Routing | Ground Truth |
|---|---|---|---|---|
| BILLING-T2-001 | We are on the Enterprise plan. Can we pay by wire transfer? | apply the Enterprise wire transfer eligibility rule to the account | answer | KB-BILLING-001 |
| BILLING-T2-002 | I am in the US but I do not see ACH as an option in my billing settings. Why not? | diagnose why ACH is not listed despite the customer being in the US | answer | KB-BILLING-001 |
| BILLING-T2-003 | My card is in USD but we get billed in EUR. What exchange rate do you use? | explain there is no fixed conversion rate and market rates apply | answer | KB-BILLING-001 |
| BILLING-T2-004 | I downgraded my plan mid-cycle. When does the lower price take effect and will I be refunded for the unused time on the higher plan? | apply the plan downgrade policy for a mid-cycle change | answer | KB-BILLING-002 |
| BILLING-T2-005 | I added 2 more seats last week in the middle of our billing cycle. How will I be charged for them? | explain prorated charges for seats added mid-cycle | answer | KB-BILLING-002 |
| BILLING-T2-006 | If I remove seats now, will my current month's invoice go down? | apply the seat removal rule that it affects future billing only | answer | KB-BILLING-002 |
| BILLING-T2-007 | We upgraded our plan mid-cycle. Should our next invoice show the prorated charge? | confirm prorated charges appear as line items on the next invoice | answer | KB-BILLING-003 |
| BILLING-T2-008 | Can you email me my invoice as a PDF attachment? | explain the billing contact gets a notification email but no PDF attachment by default | answer | KB-BILLING-003 |
| BILLING-T2-009 | My coworker is now handling our billing. How do I change who receives the invoice notification emails? | explain the billing contact can be updated in the workspace | answer | KB-BILLING-003 |
| BILLING-T2-010 | A payment failed and then I made a partial payment to settle it. Will I get a receipt for that partial payment? | apply the multiple-payments-per-cycle rule to a partial payment after dunning | answer | KB-BILLING-004 |
| BILLING-T2-011 | We received a refund last week. Is there a receipt for the refund? | explain refunds have a separate receipt on the refund transaction | answer | KB-BILLING-004 |
| BILLING-T2-012 | I need the receipt from a payment we made three months ago. Is it still available? | apply the receipt retention rule for historical payments | answer | KB-BILLING-004 |
| BILLING-T2-013 | If I update my payment method during the dunning process, will you automatically retry the failed charge? | apply the dunning restart rule when a payment method is updated | answer | KB-BILLING-005 |
| BILLING-T2-014 | My account now shows 'past due'. What does that mean and what happens next? | explain the past-due state and the restriction/suspension path | answer | KB-BILLING-005 |
| BILLING-T2-015 | If our account gets suspended because of an unpaid bill, does that cancel our subscription? | distinguish suspension from cancellation | answer | KB-BILLING-005 |
| BILLING-T2-016 | Will I be charged right away when I update my payment method on an existing subscription? | clarify that no charge is made at the time of the update | answer | KB-BILLING-006 |
| BILLING-T2-017 | My card was declined and I added a new card. When will you retry the failed charge? | explain pending retries use the valid method on file and are attempted automatically | answer | KB-BILLING-006 |
| BILLING-T2-018 | I want to switch which card is charged for our subscription. Do I need to remove the old card first? | explain the replace-card steps for switching default cards | answer | KB-BILLING-006 |
| BILLING-T2-019 | When does a 3D Secure or SCA challenge usually appear? | enumerate the situations in which a challenge may apply | answer | KB-BILLING-007 |
| BILLING-T2-020 | I completed the 3D Secure check but the charge still did not go through. What happens now? | apply the dunning path when a post-challenge payment fails | answer | KB-BILLING-007 |
| BILLING-T2-021 | I cannot complete the 3D Secure verification because I never receive the code. What can I do? | give recovery steps when the challenge cannot be completed | answer | KB-BILLING-007 |
| BILLING-T2-022 | We are based in the US. Will sales tax appear on every invoice? | apply the US sales tax rule which depends on state and local requirements | answer | KB-BILLING-008 |
| BILLING-T2-023 | My company is tax-exempt. How do I make sure no tax gets applied to our charges? | explain tax status affects tax calculation and how to provide details | answer | KB-BILLING-008 |
| BILLING-T2-024 | We changed our billing address to another state last month. Will future invoices be taxed differently? | explain tax is recalculated for the new billing address and jurisdiction | answer | KB-BILLING-008 |
| BILLING-T2-025 | Our company is relocating to another country. What changes when I update the billing country? | explain the impacts of changing the billing country | answer | KB-BILLING-009 |
| BILLING-T2-026 | My last invoice shows the wrong billing address. Can you re-issue it with the correct one? | apply the rule that already-generated invoices are not re-issued | answer | KB-BILLING-009 |
| BILLING-T2-027 | I want to change the billing address but keep my billing contact the same. Are they updated separately? | distinguish billing address from billing contact | answer | KB-BILLING-009 |
| CANCEL-T2-001 | I don't see a 'Cancel Subscription' button anywhere in our billing settings. Why not? | enterprise_account_cancellation_route | answer | KB-CANCEL-001 |
| CANCEL-T2-002 | We cancelled on June 2 but our monthly billing runs from the 15th. Do we still have access until July 15? | apply_access_until_billing_period_end | answer | KB-CANCEL-001 |
| CANCEL-T2-003 | After I confirm the cancellation, who gets the confirmation? The person who clicked the button or our billing contact? | cancellation_confirmation_recipient | answer | KB-CANCEL-001 |
| CANCEL-T2-004 | We're on annual billing and cancelled today, September 3. When exactly does our access stop? | annual_cancellation_effective_date_application | answer | KB-CANCEL-002 |
| CANCEL-T2-005 | My subscription started on the 31st of a month. If I cancel, what day does my renewal actually land on? | renewal_date_when_day_missing | answer | KB-CANCEL-002 |
| CANCEL-T2-006 | I cancelled mid-month but you still charged me for the full month. Is that right? | no_prorated_credit_on_cancellation | answer | KB-CANCEL-002 |
| CANCEL-T2-007 | Can I get my data back after the 60 days are up? | data_recovery_after_retention | answer | KB-CANCEL-003 |
| CANCEL-T2-008 | Our workspace terminated on July 15. How much longer before our data is at risk? | apply_retention_window_to_termination_date | answer | KB-CANCEL-003 |
| CANCEL-T2-009 | If we reactivate during the retention window, does our data come back with us? | reactivation_restores_retained_data | answer | KB-CANCEL-003 |
| CANCEL-T2-010 | I deleted my account by accident last month. Can you restore it? | accidental_deletion_recovery_status | answer | KB-CANCEL-004 |
| CANCEL-T2-011 | We only want to stop paying but keep the workspace so we can come back later. Should we cancel or delete? | cancel_vs_delete_for_pausing | answer | KB-CANCEL-004 |
| CANCEL-T2-012 | If we delete our account, is there any chance of getting the data back later? | deletion_is_irreversible | answer | KB-CANCEL-004 |
| CANCEL-T2-013 | We cancelled on June 10 and want to come back on July 20. Do we still get our old price and our data? | price_lock_and_data_restoration_application | answer | KB-CANCEL-005 |
| CANCEL-T2-014 | We cancelled 70 days ago. Is there any way to get the old per-user price back? | price_lock_expired_application | answer | KB-CANCEL-005 |
| CANCEL-T2-015 | I was on annual Pro when I cancelled. If I come back within the window, what price will I be charged? | annual_price_lock_rate | answer | KB-CANCEL-005 |
| CANCEL-T2-016 | We deleted our account without exporting anything first. Is there any way to recover our workflows? | recovery_after_delete_without_export | answer | KB-CANCEL-006 |
| CANCEL-T2-017 | I can't find an export option for one specific data type. What should I do? | missing_export_option_handling | answer | KB-CANCEL-006 |
| CANCEL-T2-018 | We already cancelled but haven't exported yet. Can we still export during the 60 days? | export_during_retention_window | answer | KB-CANCEL-006 |
| ENT-T2-001 | Our agreement says Net 30. When exactly is our invoice due? | Determine the invoice due date from the account's payment terms. | answer | KB-ENT-001 |
| ENT-T2-002 | We'd like to pay this quarter's invoice by wire transfer. Can we do that? | Assess wire transfer eligibility for the account. | answer | KB-ENT-001 |
| ENT-T2-003 | Our contract says annual upfront billing, but I just saw a charge on the card. How does our billing actually work? | Verify billing frequency against the signed agreement. | answer | KB-ENT-001 |
| ENT-T2-004 | We committed to 220 seats. What volume discount are we entitled to? | Determine the applicable discount from the agreement's volume-discount table. | answer | KB-ENT-002 |
| ENT-T2-005 | If we drop below our committed seat count mid-year, does our discount go away? | Determine how the discount responds to seat changes under the agreement. | answer | KB-ENT-002 |
| ENT-T2-006 | Does our negotiated discount apply to the seat add-ons we bought in July, or just to the base subscription charge? | Determine whether the discount applies to add-ons per the agreement. | answer | KB-ENT-002 |
| ENT-T2-007 | We're coming up on renewal. Who should we talk to about our seat count and contract terms? | Route renewal coordination to the assigned dedicated account manager. | answer | KB-ENT-003 |
| ENT-T2-008 | We have a billing dispute we'd like to escalate. Does our dedicated account manager handle that? | Clarify the DAM's role in escalations and normal dispute handling. | answer | KB-ENT-003 |
| ENT-T2-009 | Do we actually have a dedicated account manager assigned to our account? | Check the agreement for an assigned dedicated account manager. | answer | KB-ENT-003 |
| ENT-T2-010 | We missed the uptime target last month — can we get a service credit? | Determine eligibility for an uptime credit under the agreement. | answer | KB-ENT-004 |
| ENT-T2-011 | What uptime target applies to our account? | Determine the applicable SLA target from the agreement. | answer | KB-ENT-004 |
| ENT-T2-012 | We had about 45 minutes of downtime during what we think was scheduled maintenance. Does that count against our SLA? | Determine whether the outage counts under agreement exclusions. | answer | KB-ENT-004 |
| ENT-T2-013 | We need the latest SOC 2 report for our renewal. Can you send it over? | Process a SOC 2 documentation request under agreement terms via the account team. | answer | KB-ENT-005 |
| ENT-T2-014 | Our security team sent a questionnaire for our renewal. Who completes it and how long does it take? | Explain questionnaire coordination and response timing. | answer | KB-ENT-005 |
| ENT-T2-015 | We're evaluating a new contract and need SOC 2 documentation as part of due diligence. How do we get it? | Route a due-diligence SOC 2 request under confidentiality terms. | answer | KB-ENT-005 |
| INVOICE-T2-001 | Why is there sales tax on our invoice? We're a nonprofit and I thought we wouldn't be charged tax. | Explain when tax applies and that tax depends on jurisdiction and customer tax status | answer | KB-INVOICE-001 |
| INVOICE-T2-002 | I removed 2 seats in the middle of my billing cycle. Why wasn't I credited on this month's invoice? | Explain that seat removal affects future billing and the current cycle is not automatically credited | answer | KB-INVOICE-001 |
| INVOICE-T2-003 | We added two seats on the 12th. Can you walk me through how the prorated charge on invoice AF-2026-004821 was calculated? | Explain a prorated seat addition calculation | answer | KB-INVOICE-001 |
| INVOICE-T2-004 | Can I get a custom invoice with our PO number on our Pro plan? Our accounting team needs it. | Explain that custom invoices are Enterprise-only while PO numbers are supported on standard self-service invoices | answer | KB-INVOICE-002 |
| INVOICE-T2-005 | Our contract says net 30, but the invoice we just got shows a due date 45 days out. Which one applies? | Explain that the signed Enterprise agreement governs and the due date is computed from the invoice date per the agreement | answer | KB-INVOICE-002 |
| INVOICE-T2-006 | Our agreement is quarterly but this month we got a monthly invoice. Did something go wrong? | Explain that billing cadence is defined by the signed agreement and to confirm the agreement's terms | answer | KB-INVOICE-002 |
| INVOICE-T2-007 | I added my PO number after my latest invoice was already generated. Will that invoice get the PO on it? | Explain that a PO saved after generation appears on the next invoice | answer | KB-INVOICE-003 |
| INVOICE-T2-008 | Our Enterprise agreement requires a PO on every invoice and I need to correct the number on file. How do I get the current invoice fixed? | Explain Enterprise PO correction and corrected or replacement invoice handling | answer | KB-INVOICE-003 |
| INVOICE-T2-009 | We pay by wire transfer. What do we need to include so our payment gets matched to the right invoice? | Explain remittance requirements for wire payments | answer | KB-INVOICE-003 |
| INVOICE-T2-010 | Can you re-route our invoice emails to a different person starting next month? | Explain updating the billing contact so the next notification goes to the new address | answer | KB-INVOICE-004 |
| INVOICE-T2-011 | I changed the billing contact yesterday, but today's invoice notification still went to the old email. Why? | Explain notification timing relative to invoice generation when changing the billing contact | answer | KB-INVOICE-004 |
| INVOICE-T2-012 | Our new billing contact needs to see our past invoices. Can she pull them up, or do we need to forward them? | Explain that past invoices remain available in the Billing section for the new contact | answer | KB-INVOICE-004 |
| INVOICE-T2-013 | I'm disputing the tax on our invoice. How does AcmeFlow decide whether tax applies to us? | Explain tax verification for a disputed tax amount | answer | KB-INVOICE-005 |
| INVOICE-T2-014 | You explained the proration charge but I still think it's wrong. What happens next? | Explain escalation to Billing Operations for repeated disputes | answer | KB-INVOICE-005 |
| INVOICE-T2-015 | I want a refund for the prorated charge we got when we added seats. Can you just refund it as part of this dispute? | Explain that refunds are handled under refund policy, not granted during a dispute | answer | KB-INVOICE-005 |
| PRICING-T2-001 | Our startup has 5 people and we need unlimited workflows. Which plan should we go with? | plan_recommendation | answer | KB-PRICING-001 |
| PRICING-T2-002 | We have 40 users and need SSO/SAML. Can we buy SSO as an add-on on Pro? | enterprise_sso_eligibility | answer | KB-PRICING-001 |
| PRICING-T2-003 | We're on the Free plan and need more workflows - can we buy an add-on to bump it up? | free_plan_addon_eligibility | answer | KB-PRICING-001 |
| PRICING-T2-004 | We need audit logs for compliance but we're only a 12-person team. Is there an audit log add-on? | audit_logs_included_pro | answer | KB-PRICING-002 |
| PRICING-T2-005 | We currently have 2 active workflows and 4 users - does that fit on the free plan? | free_plan_boundary | answer | KB-PRICING-002 |
| PRICING-T2-006 | Can we get SCIM on Pro if we pay for it separately? | scim_enterprise_only | answer | KB-PRICING-002 |
| PRICING-T2-007 | We're a 3-person team on Free and hiring a 4th next month. What happens to our account? | seat_growth_upgrade | answer | KB-PRICING-003 |
| PRICING-T2-008 | I added 2 seats to our Pro plan on the 15th - what will my next invoice look like? | seat_add_proration_invoice | answer | KB-PRICING-003 |
| PRICING-T2-009 | Our Enterprise agreement has a seat commitment - can we drop below it if usage is low? | enterprise_seat_commitment | answer | KB-PRICING-003 |
| PRICING-T2-010 | Can we switch from monthly to annual billing in the middle of our cycle? | monthly_to_annual_switch | answer | KB-PRICING-004 |
| PRICING-T2-011 | We want to move from annual back to monthly - when would that actually happen? | annual_to_monthly_switch | answer | KB-PRICING-004 |
| PRICING-T2-012 | Does the annual pricing option apply to Enterprise accounts? | enterprise_billing_frequency | answer | KB-PRICING-004 |
| PRICING-T2-013 | Our workspace bills in INR - what tax line should we expect on invoices? | inr_gst_tax | answer | KB-PRICING-005 |
| PRICING-T2-014 | We changed our billing country - can we keep billing in our old currency? | billing_country_change_currency | answer | KB-PRICING-005 |
| PRICING-T2-015 | Is ACH available to us? We're based in Germany. | ach_regional_availability | answer | KB-PRICING-005 |
| PRICING-T2-016 | We're downgrading from Pro to Free this month - will we get a refund for the unused time? | downgrade_unused_time_refund | answer | KB-PRICING-006 |
| PRICING-T2-017 | I'm on annual Pro and want to downgrade to Free - when does that take effect? | annual_downgrade_effective_date | answer | KB-PRICING-006 |
| PRICING-T2-018 | After we downgrade to Free, do we lose access to audit logs right away? | downgrade_feature_revert | answer | KB-PRICING-006 |
| PRICING-T2-019 | AcmeFlow asked for my card at signup for the trial - will I be charged during the 14 days? | trial_payment_method_capture | answer | KB-PRICING-007 |
| PRICING-T2-020 | What happens if I don't have a payment method on file when my trial ends? | trial_conversion_no_payment_method | answer | KB-PRICING-007 |
| PRICING-T2-021 | I was told I get a 30-day trial by our sales rep - is that right? | trial_promotional_verification | answer | KB-PRICING-007 |
| REFUND-T2-001 | I cancelled my account last week, but I was also charged for my Pro plan two weeks ago. Can I still get a refund for that charge? | confirm a separate refundable charge posted within 30 days remains eligible even after cancellation | answer | KB-REFUND-001 |
| REFUND-T2-002 | My charge posted exactly 30 days ago today. Is today the last day I can request a refund? | apply the boundary rule that 30 days from the charge date is the last day of the window | answer | KB-REFUND-001 |
| REFUND-T2-003 | I paid my invoice on Jan 15 but didn't open the invoice until Feb 1. Does my refund window start from when I opened it? | correct the assumption that the window starts from the invoice open date; it starts from the charge posted date | answer | KB-REFUND-001 |
| REFUND-T2-004 | We're on a 5-seat Pro monthly plan at $24 per user, so $120 a month. A prorated refund was approved effective the 16th of a 30-day month. How much should we receive? | apply the prorated refund formula: 15/30 x $120 = $60 | answer | KB-REFUND-002 |
| REFUND-T2-005 | We pay annually - 8 Pro seats at the $20 effective rate, so $1,920 up front. We're 73 days into the annual term and a prorated refund was approved. What's the refund amount? | apply the annual proration formula: 292/365 x $1,920 = $1,536 | answer | KB-REFUND-002 |
| REFUND-T2-006 | I dropped 3 seats in the middle of the billing cycle. Should that produce a prorated refund for the unused seat time? | state that removing seats does not create a prorated refund on its own | answer | KB-REFUND-002 |
| REFUND-T2-007 | I'm 11 days past the 30-day refund window on my charge. Is there any way to still get a refund? | route a late request to the exception approval process with no guarantee of approval | answer | KB-REFUND-003 |
| REFUND-T2-008 | We had a rough week with outages and want a goodwill credit. Can you just issue that for us? | explain goodwill credits require escalation and approval and are assessed case by case | answer | KB-REFUND-003 |
| REFUND-T2-009 | Can a regular customer support agent approve a refund that's outside the standard policy, or does it need a manager? | state that support agents cannot issue outside-policy refunds and approval is by a Billing Operations manager | answer | KB-REFUND-003 |
| REFUND-T2-010 | I have a $120 credit balance on my workspace and my next invoice is $192. How much will I actually owe? | apply the credit automatically to the invoice: $192 - $120 = $72 due | answer | KB-REFUND-004 |
| REFUND-T2-011 | We cancelled our subscription but we still have a credit balance on the workspace. Is that money lost? | state that remaining credit balances are forfeited on cancellation unless a contract says otherwise | answer | KB-REFUND-004 |
| REFUND-T2-012 | We run two workspaces. Can I transfer the credit balance from one workspace to the other? | state that credit balances are not transferable to another workspace | answer | KB-REFUND-004 |
| REFUND-T2-013 | My ACH refund was processed 6 business days ago and hasn't appeared yet. Is that a problem? | confirm 6 business days is within the 7-10 business day ACH estimate | answer | KB-REFUND-005 |
| REFUND-T2-014 | It's been 12 business days since my card refund was processed and nothing has appeared. What should I do? | note the refund is past the 5-10 day card estimate and confirm status in the billing record before further action | answer | KB-REFUND-005 |
| REFUND-T2-015 | We're on an Enterprise plan. How long does a wire transfer refund take to land? | explain wire refund timing is per the signed agreement and may be 10-15 business days | answer | KB-REFUND-005 |
| REFUND-T2-016 | We downgraded from 8 Pro seats to 5 Pro seats on March 12. Do we get any money back for the seat time we won't use in March? | state that a downgrade takes effect next cycle and creates no partial refund for the current cycle | answer | KB-REFUND-006 |
| REFUND-T2-017 | We added 2 Pro seats mid-cycle which generated a prorated charge, then removed them later in the same cycle. Do we get a partial refund for the unused portion of that prorated charge? | state that no partial refund is created for the unused portion of a prorated seat charge after removal | answer | KB-REFUND-006 |
| REFUND-T2-018 | We got an approved exception for a $96 partial refund on our $192 monthly charge. Does the rest of the invoice still stand? | confirm a partial refund covers only the eligible portion and the remainder stays billed | answer | KB-REFUND-006 |
| TROUBLE-T2-001 | My bill came in higher than my normal monthly amount. Could it be tax or a proration? How can I tell which one it is? | Diagnose whether a higher-than-usual charge is tax, proration, or another classification | answer | KB-TROUBLE-001 |
| TROUBLE-T2-002 | I downgraded my plan last month but I was still charged the higher plan price this cycle. Is that right? | Explain that downgrades take effect at the start of the next billing cycle | answer | KB-TROUBLE-001 |
| TROUBLE-T2-003 | I removed a seat from my workspace but my bill didn't go down. Why was I charged the same amount? | Explain that removed seats normally affect future billing only | answer | KB-TROUBLE-001 |
| TROUBLE-T2-004 | One of my two charges is pending and the other is settled. Does that mean it's a double charge? | Rule out duplication when only one of the two entries is settled | answer | KB-TROUBLE-002 |
| TROUBLE-T2-005 | My January payment failed, then my February renewal went through, and both settled around the same time. Is that a duplicate charge? | Explain that a failed cycle's outstanding balance and the current renewal can settle close together as separate periods | answer | KB-TROUBLE-002 |
| TROUBLE-T2-006 | We're on an Enterprise plan and this quarter I see several charges, one per legal entity. Are these duplicates? | Explain that Enterprise split billing produces multiple charges by design | answer | KB-TROUBLE-002 |
| TROUBLE-T2-007 | My card currency and my workspace currency are both USD, but my statement amount is higher than my invoice. Why? | Explain that with matching currencies a difference points to a bank fee or a different charge, not conversion | answer | KB-TROUBLE-003 |
| TROUBLE-T2-008 | My statement shows the charge in EUR and my invoice is USD — could this be me getting double billed in two currencies? | Differentiate a single converted charge from two separate charges in different currencies | answer | KB-TROUBLE-003 |
| TROUBLE-T2-009 | Does 3D Secure verification change the amount that shows up on my bank statement? My charge went through authentication and the amount looks off. | Explain that 3D Secure can separate authorization from settlement in time but does not add a charge | answer | KB-TROUBLE-003 |
| TROUBLE-T2-010 | My statement shows a shortened merchant name and I can't see 'ACMEFLOW' in it. Could the charge still be from AcmeFlow? | Explain that banks truncate or reformat descriptors so the full text may differ | answer | KB-TROUBLE-004 |
| TROUBLE-T2-011 | I see a settled charge from ACMEFLOW on my statement but I can't find it in my workspace's invoices. Is it still mine? | Confirm the charge via amount, date and card match and locate the matching invoice | answer | KB-TROUBLE-004 |
| TROUBLE-T2-012 | I'm on the Free plan so I should never be charged, but there's an ACMEFLOW charge on my statement. What should I do? | Identify that Free plan workspaces are never charged and escalate the mismatch | answer | KB-TROUBLE-004 |
