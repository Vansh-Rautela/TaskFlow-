# Tier 1 — Direct Queries

Total: 126 queries


| Query ID | Query / Final Message | Expected Intent | Routing | Ground Truth |
|---|---|---|---|---|
| BILLING-T1-001 | What payment methods does AcmeFlow accept for Workspace subscriptions? | list supported payment methods and note availability varies by plan, region, and eligibility | answer | KB-BILLING-001 |
| BILLING-T1-002 | Do you take PayPal for AcmeFlow payments? | confirm PayPal is an accepted payment method where enabled | answer | KB-BILLING-001 |
| BILLING-T1-003 | Can I pay my AcmeFlow bill with an ACH bank transfer? | confirm ACH is available to eligible US customers | answer | KB-BILLING-001 |
| BILLING-T1-004 | When does my AcmeFlow subscription renew each month? | explain monthly renewal is on the same calendar day as the original subscription date | answer | KB-BILLING-002 |
| BILLING-T1-005 | We signed up on the 31st of January. When will we be charged in February? | explain that a renewal day that does not exist in a month bills on the final day of that month | answer | KB-BILLING-002 |
| BILLING-T1-006 | When does my annual plan get charged each year? | explain annual renewals occur on the anniversary date | answer | KB-BILLING-002 |
| BILLING-T1-007 | Where do I find my AcmeFlow invoices? | point to Workspace Settings → Billing → Invoices | answer | KB-BILLING-003 |
| BILLING-T1-008 | When is my monthly invoice available? | explain invoices are generated at cycle close and generally available the day the charge posts | answer | KB-BILLING-003 |
| BILLING-T1-009 | Do you email me my invoices as a PDF? | explain the billing contact receives a notification email but not a PDF attachment by default | answer | KB-BILLING-003 |
| BILLING-T1-010 | How do I download a receipt for a payment I made? | explain the receipt download steps from the invoice | answer | KB-BILLING-004 |
| BILLING-T1-011 | What info is shown on an AcmeFlow receipt? | describe the fields shown on a receipt | answer | KB-BILLING-004 |
| BILLING-T1-012 | How do I match a charge on my bank statement to a receipt? | explain receipts reference the payment method and match statement descriptor ACMEFLOW | answer | KB-BILLING-004 |
| BILLING-T1-013 | My payment just failed. What happens now? | explain the dunning lifecycle after a failed payment | answer | KB-BILLING-005 |
| BILLING-T1-014 | How long do I have to fix my payment method before my account gets suspended? | explain the 7-day grace period and approximate 14-day restriction/suspension timeline | answer | KB-BILLING-005 |
| BILLING-T1-015 | What happens after the 7-day grace period if I do not update my card? | explain past-due state and subsequent restriction/suspension | answer | KB-BILLING-005 |
| BILLING-T1-016 | How do I update the credit card on my AcmeFlow account? | provide the payment method update steps | answer | KB-BILLING-006 |
| BILLING-T1-017 | Can I switch my AcmeFlow payment method to PayPal? | explain switching to PayPal where enabled for the account and region | answer | KB-BILLING-006 |
| BILLING-T1-018 | My card expired. How do I add the new card? | explain adding a new card and setting it as default | answer | KB-BILLING-006 |
| BILLING-T1-019 | What is 3D Secure and why is AcmeFlow asking me to verify my card? | explain 3D Secure/SCA as a cardholder authentication step | answer | KB-BILLING-007 |
| BILLING-T1-020 | I got a one-time code from my bank when adding my card. What should I do with it? | explain completing the 3D Secure/SCA challenge | answer | KB-BILLING-007 |
| BILLING-T1-021 | My bank asked me to approve an AcmeFlow charge in their app. Is that normal? | confirm the app-approval prompt is a normal 3D Secure/SCA step | answer | KB-BILLING-007 |
| BILLING-T1-022 | Does AcmeFlow charge sales tax? | explain supported tax types and that treatment varies by jurisdiction | answer | KB-BILLING-008 |
| BILLING-T1-023 | How do I add my GST registration number to AcmeFlow? | explain the Tax Details entry steps | answer | KB-BILLING-008 |
| BILLING-T1-024 | Do you apply VAT for customers in Europe? | confirm VAT applies in VAT jurisdictions including many European countries | answer | KB-BILLING-008 |
| BILLING-T1-025 | How do I change my billing address on AcmeFlow? | explain the billing address update steps | answer | KB-BILLING-009 |
| BILLING-T1-026 | We just moved to a new state. How do I update the billing address on our account? | explain updating the billing address and that it affects future invoices and tax | answer | KB-BILLING-009 |
| BILLING-T1-027 | If I update my billing address, will my existing invoices change to show the new address? | explain invoices already generated are not re-issued | answer | KB-BILLING-009 |
| CANCEL-T1-001 | How do I cancel my AcmeFlow subscription? | self_serve_cancellation_steps | answer | KB-CANCEL-001 |
| CANCEL-T1-002 | Can I cancel on my own or do I have to email someone? I just want to stop being charged next month. | confirm_cancellation_is_self_serve | answer | KB-CANCEL-001 |
| CANCEL-T1-003 | where do i find the cancel option in the app? can't seem to locate it | cancellation_navigation_path | answer | KB-CANCEL-001 |
| CANCEL-T1-004 | If I cancel my monthly plan today, when does the cancellation actually take effect? | cancellation_effective_date | answer | KB-CANCEL-002 |
| CANCEL-T1-005 | Does cancelling give me money back for the days I didn't use this month? | no_prorated_refund_on_cancellation | answer | KB-CANCEL-002 |
| CANCEL-T1-006 | I'm on the annual plan. If I cancel halfway through the year do I keep access until the year is up? | annual_cancellation_effective_date | answer | KB-CANCEL-002 |
| CANCEL-T1-007 | How long do you keep my data after I cancel my subscription? | data_retention_window | answer | KB-CANCEL-003 |
| CANCEL-T1-008 | What happens to my workspace data after the retention window ends? | post_retention_deletion | answer | KB-CANCEL-003 |
| CANCEL-T1-009 | Is my data deleted right away when I cancel? I'm worried I'll lose everything. | cancellation_does_not_delete_data | answer | KB-CANCEL-003 |
| CANCEL-T1-010 | What's the difference between cancelling my subscription and deleting my account? | cancel_vs_delete_distinction | answer | KB-CANCEL-004 |
| CANCEL-T1-011 | If I want to close my account for good, what's the right order to do things? | recommended_cancel_export_delete_order | answer | KB-CANCEL-004 |
| CANCEL-T1-012 | Does cancelling my subscription delete my data? | cancellation_keeps_data | answer | KB-CANCEL-004 |
| CANCEL-T1-013 | I cancelled a couple weeks ago. Can I sign back up for Pro? | reactivation_possible | answer | KB-CANCEL-005 |
| CANCEL-T1-014 | If I come back within 60 days of cancelling, will I keep paying the same price per user as before? | price_lock_window | answer | KB-CANCEL-005 |
| CANCEL-T1-015 | I cancelled 3 months ago. If I resubscribe now, will I get my old price back? | price_lock_expired | answer | KB-CANCEL-005 |
| CANCEL-T1-016 | How do I export my workflows before I cancel? | data_export_steps | answer | KB-CANCEL-006 |
| CANCEL-T1-017 | If I cancel, do you automatically send me an export of all my data? | no_automatic_export_on_cancel | answer | KB-CANCEL-006 |
| CANCEL-T1-018 | What kinds of data can I export from my workspace? | exportable_data_types | answer | KB-CANCEL-006 |
| ENT-T1-001 | Is there a standard Enterprise price for AcmeFlow Workspace? I keep seeing different numbers on different pages. | Determine whether a universal Enterprise price exists. | answer | KB-ENT-001 |
| ENT-T1-002 | What kinds of billing terms can be negotiated in an enterprise agreement? | List the customizable billing structures available under an enterprise agreement. | answer | KB-ENT-001 |
| ENT-T1-003 | Can enterprise customers pay by wire transfer? | Confirm wire transfer availability for enterprise accounts. | answer | KB-ENT-001 |
| ENT-T1-004 | Does AcmeFlow have a standard schedule of volume-discount thresholds? | Establish that no universal volume-discount tier schedule exists. | answer | KB-ENT-002 |
| ENT-T1-005 | What is the general structure of a volume discount for enterprise customers? | Explain how volume discounts are typically structured. | answer | KB-ENT-002 |
| ENT-T1-006 | What happens if our enterprise agreement doesn't mention a volume discount at all? | Explain billing when no volume-discount provision exists. | answer | KB-ENT-002 |
| ENT-T1-007 | What does a dedicated account manager actually do for an enterprise customer? | Describe the role and responsibilities of a dedicated account manager. | answer | KB-ENT-003 |
| ENT-T1-008 | If we have a dedicated account manager, do we still open tickets for technical incidents? | Clarify that the dedicated account manager does not replace normal support channels. | answer | KB-ENT-003 |
| ENT-T1-009 | Is a dedicated account manager included for every enterprise customer? | Confirm DAM inclusion depends on the signed agreement. | answer | KB-ENT-003 |
| ENT-T1-010 | What is the standard enterprise SLA uptime target for AcmeFlow Workspace? | State the standard enterprise SLA uptime target. | answer | KB-ENT-004 |
| ENT-T1-011 | How is downtime measured for SLA purposes? | Explain how uptime and downtime are measured. | answer | KB-ENT-004 |
| ENT-T1-012 | Do Free or Pro plans come with an SLA? | Confirm self-service plans have no SLA. | answer | KB-ENT-004 |
| ENT-T1-013 | Does AcmeFlow provide SOC 2 documentation to enterprise customers? | Confirm SOC 2 documentation is available under controlled terms. | answer | KB-ENT-005 |
| ENT-T1-014 | How are SOC 2 reports shared with customers? | Explain the controlled distribution channel for SOC 2 reports. | answer | KB-ENT-005 |
| ENT-T1-015 | Who coordinates the response to a security questionnaire? | Explain how security questionnaire responses are coordinated. | answer | KB-ENT-005 |
| INVOICE-T1-001 | Why does my invoice say $240.80 when I have 8 Pro seats at $24 a month? 8 times 24 is 192, so where is the extra coming from? | Explain why the invoice total exceeds the base seat charge (prorated seat addition and tax line items) | answer | KB-INVOICE-001 |
| INVOICE-T1-002 | Can you explain what each line on my AcmeFlow invoice means? I see a subscription charge, a proration, sales tax, and a negative credit amount. | Explain invoice line item categories | answer | KB-INVOICE-001 |
| INVOICE-T1-003 | What is the format of an AcmeFlow invoice ID? And how is that different from a receipt reference? | Explain invoice and receipt reference formats | answer | KB-INVOICE-001 |
| INVOICE-T1-004 | We're an Enterprise customer. Do you support custom invoices with our purchase order number and net 45 payment terms? | Confirm Enterprise custom invoices and net payment terms are supported | answer | KB-INVOICE-002 |
| INVOICE-T1-005 | Can AcmeFlow bill us in EUR instead of USD? Our parent company is in Germany. | Explain contract currency for Enterprise invoicing | answer | KB-INVOICE-002 |
| INVOICE-T1-006 | Our signed Enterprise agreement is quarterly. Why does our invoice show a due date 30 days from the invoice date instead of charging my card? | Explain net payment terms and quarterly billing under an Enterprise agreement | answer | KB-INVOICE-002 |
| INVOICE-T1-007 | How do I add a purchase order number to my invoices? | Explain how to provide a PO number on a self-service workspace | answer | KB-INVOICE-003 |
| INVOICE-T1-008 | If I add a PO number to my account, will my invoice amount change? | Confirm a PO number is a reference only and does not change charges | answer | KB-INVOICE-003 |
| INVOICE-T1-009 | I saved our PO number on the 20th but my invoice that came out this month doesn't show it. What's going on? | Explain that the PO number appears only on invoices generated after it is saved | answer | KB-INVOICE-003 |
| INVOICE-T1-010 | How do I change the billing contact for our workspace so invoice emails go to someone else? | Explain how to update the billing contact | answer | KB-INVOICE-004 |
| INVOICE-T1-011 | Who receives the invoice notification emails for our workspace? | Explain that the billing contact is the recipient of invoice notifications | answer | KB-INVOICE-004 |
| INVOICE-T1-012 | After I update the billing contact, will our old invoices be re-sent to the new email? | Confirm past invoices are not re-sent to a new billing contact | answer | KB-INVOICE-004 |
| INVOICE-T1-013 | I think there's an error on my invoice. What do you need from me to look into it? | Request the information needed to triage an invoice dispute | answer | KB-INVOICE-005 |
| INVOICE-T1-014 | Once you process a refund for an invoice, how long until it shows up on my credit card? | Explain refund processing timeframes | answer | KB-INVOICE-005 |
| INVOICE-T1-015 | I got an invoice and a receipt with different reference numbers. Are those two separate charges? | Explain the difference between an invoice and its associated receipt | answer | KB-INVOICE-005 |
| PRICING-T1-001 | What are the three AcmeFlow plans and how is each one priced? | compare_plan_pricing | answer | KB-PRICING-001 |
| PRICING-T1-002 | how many users can i add on the free plan? | free_plan_seat_limit | answer | KB-PRICING-001 |
| PRICING-T1-003 | Which plan gives us a dedicated account manager? | plan_support_levels | answer | KB-PRICING-001 |
| PRICING-T1-004 | Do audit logs come with every plan or just some? | feature_availability_audit_logs | answer | KB-PRICING-002 |
| PRICING-T1-005 | Is standard analytics available on the Free plan? | feature_availability_analytics | answer | KB-PRICING-002 |
| PRICING-T1-006 | Does Pro come with an SLA? | sla_availability | answer | KB-PRICING-002 |
| PRICING-T1-007 | How many seats are included with the free plan? | free_plan_seat_inclusion | answer | KB-PRICING-003 |
| PRICING-T1-008 | If I add a seat partway through my billing cycle, when does the new price apply? | seat_add_proration_timing | answer | KB-PRICING-003 |
| PRICING-T1-009 | Can I run a Pro workspace with just one person? | pro_minimum_seats | answer | KB-PRICING-003 |
| PRICING-T1-010 | whats the difference between paying monthly vs annual for pro? | compare_billing_frequency | answer | KB-PRICING-004 |
| PRICING-T1-011 | When exactly does my monthly subscription renew each month? | monthly_renewal_timing | answer | KB-PRICING-004 |
| PRICING-T1-012 | How much would Pro cost for 10 seats if we pay annually? | annual_cost_calculation | answer | KB-PRICING-004 |
| PRICING-T1-013 | Which currencies does AcmeFlow bill in? | supported_currencies | answer | KB-PRICING-005 |
| PRICING-T1-014 | How is my charge converted if I bill in EUR instead of USD? | currency_conversion_process | answer | KB-PRICING-005 |
| PRICING-T1-015 | Where do I change the currency my workspace is billed in? | currency_selection_location | answer | KB-PRICING-005 |
| PRICING-T1-016 | How quickly does a plan upgrade take effect? | upgrade_effective_date | answer | KB-PRICING-006 |
| PRICING-T1-017 | When does a downgrade take effect on my account? | downgrade_effective_date | answer | KB-PRICING-006 |
| PRICING-T1-018 | If we downgrade from Pro to Free, how long do we keep Pro features? | downgrade_feature_retention | answer | KB-PRICING-006 |
| PRICING-T1-019 | How long is the AcmeFlow trial? | trial_duration | answer | KB-PRICING-007 |
| PRICING-T1-020 | What happens when my 14-day trial ends? | trial_conversion | answer | KB-PRICING-007 |
| PRICING-T1-021 | Can I cancel during the trial without being charged? | trial_cancellation | answer | KB-PRICING-007 |
| REFUND-T1-001 | How long is your refund window and when does the clock start for a charge? | explain the 30-day refund window and that it is measured from the charge posted date | answer | KB-REFUND-001 |
| REFUND-T1-002 | I cancelled my subscription - do I automatically get a refund for the time I won't be using? | state that cancellation does not automatically create a refund and unused time is not automatically refundable | answer | KB-REFUND-001 |
| REFUND-T1-003 | Which charges are actually eligible for a standard refund under AcmeFlow's policy? | list eligible charges under the standard 30-day refund policy | answer | KB-REFUND-001 |
| REFUND-T1-004 | Can you explain the formula you use to calculate a prorated refund? | explain the prorated refund formula and its inputs | answer | KB-REFUND-002 |
| REFUND-T1-005 | When you work out proration, how many days do you count a monthly billing period as? | state the calculation assumption of 30 days for a monthly period and 365 days for annual | answer | KB-REFUND-002 |
| REFUND-T1-006 | Does cancelling my plan automatically give me a prorated refund for the rest of the month? | state that prorated refunds are the exception and cancellation alone creates none | answer | KB-REFUND-002 |
| REFUND-T1-007 | My request is outside the 30-day window. Is there any way to get a refund anyway? | explain that requests after the window closes may only proceed through the Refund Exception Approval policy | answer | KB-REFUND-003 |
| REFUND-T1-008 | Who is allowed to approve a refund that isn't covered by the standard policy? | identify the appropriate approver for refund exceptions | answer | KB-REFUND-003 |
| REFUND-T1-009 | What is a goodwill credit and how does AcmeFlow give one out? | explain goodwill credits granted for service or billing issues and how they are held | answer | KB-REFUND-003 |
| REFUND-T1-010 | When you refund me, does the money go back to my card or as a credit on my account? | explain refunds return to the original payment method or become a workspace credit balance | answer | KB-REFUND-004 |
| REFUND-T1-011 | Can I withdraw the credit balance on my workspace as cash? | state that credit balances have no cash-out value | answer | KB-REFUND-004 |
| REFUND-T1-012 | What happens to my remaining credit balance if I cancel my subscription? | explain credit balances are forfeited on cancellation unless a contract says otherwise | answer | KB-REFUND-004 |
| REFUND-T1-013 | Roughly how long does a refund to a credit card take to show up? | provide the card refund timeframe of 5-10 business days | answer | KB-REFUND-005 |
| REFUND-T1-014 | How long do PayPal refunds usually take? | provide the PayPal refund timeframe of 5-7 business days | answer | KB-REFUND-005 |
| REFUND-T1-015 | When does the refund timing actually start counting from? | explain refund timeframes start from when AcmeFlow processes the refund, in business days | answer | KB-REFUND-005 |
| REFUND-T1-016 | If I remove seats from my Pro workspace, will I get any money back for them? | state that removing seats affects future billing only and creates no partial refund | answer | KB-REFUND-006 |
| REFUND-T1-017 | Does downgrading my plan trigger a partial refund for the time I won't use? | state that a downgrade takes effect next cycle and does not create a partial refund | answer | KB-REFUND-006 |
| REFUND-T1-018 | In which situations can a partial refund actually be issued? | list the specific situations where a partial refund may apply | answer | KB-REFUND-006 |
| TROUBLE-T1-001 | I got charged an extra $30.40 this month on top of my usual $144 Pro bill and I have no idea why. Can you look into it? | Investigate an unexpected charge and explain the prorated seat addition | answer | KB-TROUBLE-001 |
| TROUBLE-T1-002 | Why did my renewal charge come in higher than normal? The invoice has a line item that says 'overdue period' — what is that? | Explain a previous balance from a failed cycle being collected at renewal | answer | KB-TROUBLE-001 |
| TROUBLE-T1-003 | I cancelled my subscription last month but I was charged again on the 1st. Why was I charged after cancelling? | Explain that paid access continues until the end of the current billing period after cancellation | answer | KB-TROUBLE-001 |
| TROUBLE-T1-004 | I have two settled charges of $192.00 for the same month on my card. Was I double charged? | Investigate whether two settled charges covering the same period are a genuine double charge | answer | KB-TROUBLE-002 |
| TROUBLE-T1-005 | There's a pending charge from AcmeFlow on my card that I didn't expect. Should I be worried that it will post? | Explain that a pending entry is an authorization that will settle or fall off | answer | KB-TROUBLE-002 |
| TROUBLE-T1-006 | When I added my card to my workspace I saw a temporary hold on it. Is that a real charge? | Explain a pre-authorization hold placed when a payment method is added | answer | KB-TROUBLE-002 |
| TROUBLE-T1-007 | My bank statement shows my charge in EUR but my invoice is in USD. Why did you charge me in euros? | Explain that the card currency differs from the workspace currency and a conversion is expected | answer | KB-TROUBLE-003 |
| TROUBLE-T1-008 | Why doesn't the amount on my bank statement match my AcmeFlow invoice? The invoice says $192.00 but my bank shows a different number. | Explain conversion timing and processor or bank fees behind the statement amount | answer | KB-TROUBLE-003 |
| TROUBLE-T1-009 | My Pro invoice is $192.00 in USD but my EUR card statement shows €176.20. Is that amount correct? | Confirm that a converted statement amount is correct and needs no adjustment | answer | KB-TROUBLE-003 |
| TROUBLE-T1-010 | I don't recognize a charge on my bank statement. What should I do? | Start the unrecognized charge investigation by gathering statement details | answer | KB-TROUBLE-004 |
| TROUBLE-T1-011 | My statement just says 'ACMEFLOW' but my invoice says 'AcmeFlow Inc.' Is this really you? | Explain that ACMEFLOW is the processor descriptor while AcmeFlow Inc. is the legal entity on invoices | answer | KB-TROUBLE-004 |
| TROUBLE-T1-012 | There's a $192.00 charge from ACMEFLOW on my statement that I don't recognize. Is that AcmeFlow or is it someone else? | Confirm an AcmeFlow charge via descriptor and matching invoice details | answer | KB-TROUBLE-004 |
