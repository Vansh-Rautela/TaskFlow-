---
document_id: KB-BILLING-006
title: Payment Method Update
category: Billing & Payments
subcategory: Payment Methods
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
  - payment method
  - credit card
  - update card
  - ACH
  - PayPal
  - billing
---

# Payment Method Update

This article explains how to update, add, or remove a payment method on your AcmeFlow Workspace subscription. Keeping a valid payment method on file prevents failed payments and interruptions to your service.

## When to Update Your Payment Method

Common reasons to update your payment method:

- Your card expired or was replaced.
- Your card was declined on a recent charge.
- You want to switch from a card to another accepted method.
- Your workspace's billing contact changed and the new contact manages payments.
- You received a notification about a failed payment.

## How to Update Your Payment Method

1. Sign in to AcmeFlow Workspace.
2. Open **Workspace Settings → Billing**.
3. Select **Payment Method**.
4. Choose **Add Payment Method** or **Edit** next to the existing method.
5. Enter the new method details and confirm.

The new method is used for the next charge. For an existing subscription, no charge is made at the time you update the method.

## Changing the Card Used for Payments

To replace the card on file:

1. Add the new card following the steps above.
2. Set it as the default or remove the old card.

Any pending retry of a failed payment will use the valid method on file.

**Example:** A Pro workspace's card ending in 4821 was declined on the cycle close. The billing contact adds a new card ending in 9034. The next automatic retry is attempted against the new card, and the balance is cleared.

## Switching to ACH or PayPal

- **ACH** — Available to eligible US customers. Select ACH as the payment method and complete the bank account setup.
- **PayPal** — Available where PayPal is enabled for your account and region. You will be asked to authorize the payment through your PayPal account.

If the method you want is not listed, it is not available for your plan or region.

## Updating the Payment Method During a Failed Payment

If a payment failed and you are in the dunning process:

- Update the payment method as soon as possible during the grace period (up to 7 days from the first failure).
- A new payment attempt is made automatically where available.
- If the grace period passes without a valid payment method, the subscription enters a past-due state, and restriction and suspension are possible around 14 days from the first failure.

**Example:** A workspace is notified of a failed $192.00 charge on its monthly cycle close. The billing contact updates the payment method on day 2 of the grace period. The retry succeeds and the subscription continues normally.

## Payment Method Availability

Not every payment method is available to every plan or region. Availability depends on plan, region, and eligibility:

- Credit cards (Visa, Mastercard, American Express; Discover where supported)
- Debit cards where supported
- ACH for eligible US customers
- PayPal where enabled
- Wire transfer for qualifying Enterprise customers

## Enterprise Accounts

- For qualifying Enterprise customers, wire transfer is available under the signed agreement.
- The customer's signed Enterprise agreement takes precedence over the standard self-service policy where the two differ.

## Related Documentation

- Supported Payment Methods
- Failed Payment & Dunning Process
- Billing Cycle Explanation
- Invoice Generation & Delivery
- Billing Address Changes
- Enterprise Contract Billing