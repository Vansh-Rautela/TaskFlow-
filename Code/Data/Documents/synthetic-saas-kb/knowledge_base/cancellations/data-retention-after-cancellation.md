---
document_id: KB-CANCEL-003
title: Data Retention After Cancellation
category: Cancellations & Account Management
subcategory: Data Retention
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
  - data retention
  - cancellation
  - retention window
  - export
  - deletion
  - irreversible
---

# Data Retention After Cancellation

This policy defines how long workspace data is retained after a subscription terminates, what the retention window covers, and what happens when the window ends.

## The 60-Day Retention Window

After a subscription terminates, workspace data is retained for 60 days. The 60-day period is measured from the date the subscription terminates, which is the end of the current billing period for a self-service cancellation.

During the retention window, the workspace and its data are not immediately deleted. The intent of the window is to give customers time to export data or to reactivate the subscription.

## What the Retention Window Covers

The retention window covers the workspace data that was present at subscription termination, including workflows, configurations, and associated data stored in the workspace. Customers should export any required data before deletion is requested.

## What Happens After the Retention Window

When the retention window ends without reactivation or data export, the workspace data is subject to deletion. Deletion after the retention period may be irreversible. Data that is deleted cannot be restored by the customer or by support.

## Cancellation Is Not Deletion

Cancellation stops future renewal; it does not delete the workspace. Workspace data is retained for the 60-day window after the subscription terminates. Account deletion is a separate action that removes the account and its data. See Account Deletion vs Subscription Cancellation.

**Example:** A Pro workspace on monthly billing terminates on July 15. The workspace data is retained through approximately September 13 (60 days after termination). If the admin exports the data on August 1, the export covers the workspace data retained at that point. If neither reactivation nor export occurs, the data is subject to deletion after the window and may be irreversible.

## Reactivation During the Window

Reactivating the subscription within the 60-day retention window restores the workspace data. See Reactivation & Price Locking for how price and access are handled on return.

## Enterprise Retention Terms

Enterprise contracts may define different retention periods. A signed Enterprise agreement may provide a longer or shorter retention window than the standard 60 days, or may define retention obligations separately. The customer's signed Enterprise agreement takes precedence over the standard self-service policy where the two differ. Support agents must not state a fixed retention figure for an Enterprise account without checking the agreement.

## Agent Guidance

When a customer asks whether a specific workspace's data is still available or how much longer it will be retained, do not answer from memory. Retrieve the account's actual termination date and subscription status from the billing system, then apply the retention window to that date.

## Related Documentation

- Cancellation Effective Date
- Account Deletion vs Subscription Cancellation
- Data Export Before Cancellation
- Reactivation & Price Locking
- Self-Serve Cancellation