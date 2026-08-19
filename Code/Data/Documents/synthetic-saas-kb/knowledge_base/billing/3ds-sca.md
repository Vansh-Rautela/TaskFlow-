---
document_id: KB-BILLING-007
title: 3D Secure / SCA
category: Billing & Payments
subcategory: Card Payments
document_type: Customer Help Center Article
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
  - 3D Secure
  - SCA
  - strong customer authentication
  - card verification
  - billing
---

# 3D Secure / SCA

This article explains 3D Secure and Strong Customer Authentication (SCA) checks that may apply when you pay for AcmeFlow Workspace with a card, and what to do if a check interrupts your payment.

## What 3D Secure / SCA Is

3D Secure is a cardholder authentication step that some card issuers and regions require. SCA (Strong Customer Authentication) is a similar requirement in certain regions, including parts of Europe. Together they add an extra verification step to confirm the payment is authorized by the cardholder.

When a check applies, you may be asked to:

- Confirm the payment in your bank's or card issuer's app
- Enter a one-time code sent by your bank
- Approve the charge on a confirmation screen

## When a Check May Apply

A 3D Secure or SCA challenge may apply:

- When you first add a card to your AcmeFlow Workspace
- When a subscription charge is initiated at a billing cycle close
- When a charge is retried after a failed payment
- Depending on your card issuer and region

Whether a check appears is controlled by the card issuer and the payment processor; AcmeFlow does not decide when a challenge is shown.

## What to Do If a Check Interrupts a Payment

1. Complete the challenge shown by your bank or card issuer (app confirmation, one-time code, or approval screen).
2. Return to the AcmeFlow Workspace Billing section and confirm the payment status.
3. If the payment did not go through, the standard dunning process applies and a retry may occur.

If you did not receive a code or prompt, check your bank's app and registered phone number for the notification.

## If You Cannot Complete the Check

If you cannot complete the verification:

- Update the payment method to a card you can verify, or another supported method where available.
- Ensure the billing address on file matches the card's registered address.
- Contact your card issuer if the challenge is not being delivered.

**Example:** A Pro workspace adds a new card ending in 9034. The card issuer requires a 3D Secure confirmation, which the billing contact approves in the bank's app. The card is then active and the next cycle charge posts normally.

## What This Means for Support

When a customer reports a blocked or unconfirmed charge, the agent should verify:

- The workspace and subscription ID
- The invoice and charge date for the affected cycle
- The payment method and whether a challenge was required
- The payment status and whether a retry is pending

A 3D Secure check is not a declined payment by itself; the payment may still succeed once the customer completes the challenge.

**Example:** A customer reports that a $192.00 charge "disappeared" after a card challenge. The agent retrieves the workspace, invoice, and charge status. If the challenge was not completed, the charge may not have posted, and a retry or re-attempt will occur.

## Related Documentation

- Supported Payment Methods
- Payment Method Update
- Failed Payment & Dunning Process
- Invoice Generation & Delivery
- Why Was I Charged?
- Double Charge Investigation