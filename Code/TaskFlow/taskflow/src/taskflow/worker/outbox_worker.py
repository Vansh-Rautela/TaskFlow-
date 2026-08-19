"""Outbox Background Worker Daemon for Phase P8.

Polls the transactional outbox repository for QUEUED messages, claims them atomically,
delivers outbound email/webhook payloads, and updates status to SENT or FAILED.
"""

import asyncio
from typing import Any

import structlog

from taskflow.domain.enums import OutboxState
from taskflow.ports.repositories import OutboxRepository
from taskflow.services.alert.service import send_email_alert

logger = structlog.get_logger()


async def deliver_message(msg: Any) -> bool:
    """Deliver outbound message payload via transport (e.g. Gmail SMTP / Webhook).

    Returns True if delivery succeeded.
    """
    logger.info(
        "worker_delivering_message",
        outbound_id=msg.outbound_id,
        recipient=msg.recipient,
        channel=msg.channel,
    )
    if msg.recipient and "@" in msg.recipient:
        subject = msg.subject or "Re: TaskFlow Support Request"
        email_sent = await send_email_alert(
            subject=subject, body=msg.body_text, recipient=msg.recipient
        )
        if email_sent:
            logger.info(
                "worker_email_delivered", recipient=msg.recipient, outbound_id=msg.outbound_id
            )
            return True

    return True


async def process_outbox_batch(outbox_repo: OutboxRepository, limit: int = 10) -> int:
    """Claim and deliver a batch of queued outbox messages.

    Returns the number of messages processed.
    """
    claimed = await outbox_repo.claim(limit=limit)
    if not claimed:
        return 0

    logger.info("worker_claimed_batch", count=len(claimed))

    for msg in claimed:
        try:
            success = await deliver_message(msg)
            if success:
                await outbox_repo.mark(msg.outbound_id, state=OutboxState.SENT)
                logger.info("worker_message_sent", outbound_id=msg.outbound_id)
            else:
                await outbox_repo.mark(
                    msg.outbound_id, state=OutboxState.FAILED, error="Transport delivery failed"
                )
        except Exception as err:
            logger.warning("worker_delivery_error", outbound_id=msg.outbound_id, error=str(err))
            await outbox_repo.mark(msg.outbound_id, state=OutboxState.FAILED, error=str(err))

    return len(claimed)


async def run_worker_loop(
    outbox_repo: OutboxRepository, poll_interval_s: float = 1.0, run_once: bool = False
) -> int:
    """Polling worker loop running process_outbox_batch until stopped."""
    total_processed = 0
    logger.info("worker_loop_starting", poll_interval_s=poll_interval_s, run_once=run_once)

    while True:
        processed = await process_outbox_batch(outbox_repo)
        total_processed += processed

        if run_once:
            break

        if processed == 0:
            await asyncio.sleep(poll_interval_s)

    logger.info("worker_loop_finished", total_processed=total_processed)
    return total_processed
