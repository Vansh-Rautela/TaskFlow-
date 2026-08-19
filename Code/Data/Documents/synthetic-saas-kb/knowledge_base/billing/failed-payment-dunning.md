---
document_id: KB-BILLING-005
title: Failed Payment & Dunning Process
category: Billing & Payments
subcategory: Failed Payments
document_type: Billing Policy
audience:
  - Customer Support
  - Billing Operations
status: active
version: "1.0"
effective_date: "2026-01-01"
last_reviewed: "2026-07-01"
owner: Billing Operations
product: AcmeFlow Workspace
tags:
  - failed payment
  - dunning
  - retry
  - grace period
  - past due
  - suspension
  - billing policy
---

# Failed Payment & Dunning Process

This policy describes what happens when a subscription payment for AcmeFlow Workspace fails, and the steps that follow from the first failed payment through restriction and suspension. It applies to standard self-service subscriptions.

## Dunning Lifecycle

A failed payment moves through the following lifecycle:

1. **Payment Attempt** — The charge is attempted at the billing cycle close.
2. **Payment Failure** — The charge fails (for example, a declined card, insufficient funds, or an expired card).
3. **Customer Notification** — The workspace billing contact is notified of the failure.
4. **Automatic Retry** — AcmeFlow automatically retries the payment.
5. **Payment Method Update** — The customer updates the payment method on file.
6. **Additional Retry / Grace Period** — Further retries continue during the grace period.
7. **Past-Due State** — If no valid payment method is available after the grace period, the subscription enters a past-due state.
8. **Restriction / Suspension** — Continued non-payment may lead to restriction and then suspension.

## Standard (Self-Service) Schedule

For standard self-service subscriptions:

- The customer is notified on the first failure.
- Automatic retries continue during a grace period of **up to 7 days** from the first failure.
- If no valid payment method is available after the grace period, the subscription enters a **past-due** state.
- Continued non-payment may lead to **restriction then suspension**, typically around **14 days** from the first failure. This timing is approximate and is subject to plan and agreement.
- Exact retry timings are documented only where a specific document defines them.

**Example:** A Pro workspace's monthly charge of $192.00 fails on the cycle close date because the card was declined. The billing contact is notified the same day, and AcmeFlow automatically retries over the following days. If the card is not updated within the 7-day grace period, the subscription moves to a past-due state, with restriction and suspension possible around day 14.

## Updating the Payment Method

The fastest way to resolve a failed payment is to update the payment method:

1. Sign in to AcmeFlow Workspace.
2. Open **Workspace Settings → Billing**.
3. Select **Payment Method** and add a valid method.
4. A new payment attempt is made automatically where available.

Updating the payment method during the grace period restarts the collection flow and avoids restriction or suspension.

## Restriction and Suspension

- **Restriction** — The workspace's ability to make certain changes may be limited until payment is resolved.
- **Suspension** — Access to the subscription may be suspended if the account remains unpaid.
- Restriction and suspension do not cancel the subscription; they are collection measures. The subscription still needs to be cancelled separately if the customer wants to stop it.

## What Support Should Verify

When a customer reports a failed payment, the agent should retrieve and confirm:

- Workspace ID
- Subscription status and plan
- The billing cycle and the charge date
- The invoice for the failed cycle
- The payment method on file and its status
- Where in the dunning lifecycle the account is (grace period, past-due, restriction, suspension)

The agent must not assume which retry has been attempted; the account's actual state should be verified.

## Policy Exceptions

- The customer's signed Enterprise agreement takes precedence over the standard self-service policy where the two differ.
- Enterprise agreements may define different schedules, grace periods, and payment terms.
- Restriction and suspension timing is approximate and subject to plan and agreement; it is never guaranteed.

## Related Documentation

- Payment Method Update
- Billing Cycle Explanation
- Supported Payment Methods
- Invoice Generation & Delivery
- Why Was I Charged?
- Enterprise Contract Billing