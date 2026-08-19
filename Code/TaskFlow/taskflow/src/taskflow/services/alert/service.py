"""Multi-Channel Alerting Service for TaskFlow.

Dispatches instant alerts for items requiring human review or escalations across:
1. Gmail SMTP Email (using GMAIL_USER and GMAIL_APP_PASSWORD)
2. Telegram Bot (using TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID)
3. Slack Webhook (using SLACK_WEBHOOK_URL)
4. Custom HTTP Webhook (using ALERT_WEBHOOK_URL)
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import httpx
import structlog

from taskflow.config.settings import settings
from taskflow.domain.models import ReviewItem

logger = structlog.get_logger()


async def send_email_alert(subject: str, body: str) -> bool:
    """Send an instant email notification using Gmail SMTP credentials."""
    user = settings().gmail_user
    password = settings().gmail_app_password
    to_email = settings().ops_email or user

    if not user or not password:
        logger.debug("email_alert_skipped", reason="GMAIL_USER or GMAIL_APP_PASSWORD not set")
        return False

    try:
        msg = MIMEMultipart()
        msg["From"] = user
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain", "utf-8"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(user, password)
            server.send_message(msg)

        logger.info("email_alert_sent", recipient=to_email, subject=subject)
        return True
    except Exception as err:
        logger.warning("email_alert_failed", error=str(err))
        return False


async def send_telegram_alert(text: str) -> bool:
    """Send instant push alert to Telegram chat via Bot API."""
    token = settings().telegram_bot_token
    chat_id = settings().telegram_chat_id

    if not token or not chat_id:
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            res = await client.post(url, json=payload)
            return res.status_code == 200
    except Exception as err:
        logger.warning("telegram_alert_failed", error=str(err))
        return False


async def send_slack_alert(text: str) -> bool:
    """Send alert message to Slack incoming webhook."""
    webhook_url = settings().slack_webhook_url
    if not webhook_url:
        return False

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            res = await client.post(webhook_url, json={"text": text})
            return res.status_code == 200
    except Exception as err:
        logger.warning("slack_alert_failed", error=str(err))
        return False


async def send_custom_webhook_alert(payload: dict) -> bool:
    """Send alert payload to generic HTTP Webhook URL."""
    webhook_url = settings().alert_webhook_url
    if not webhook_url:
        return False

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            res = await client.post(webhook_url, json=payload)
            return res.status_code in (200, 201, 202, 204)
    except Exception as err:
        logger.warning("custom_webhook_alert_failed", error=str(err))
        return False


async def dispatch_alert(item: ReviewItem) -> dict[str, bool]:
    """Dispatch alert across all active alert channels for a review item."""
    subject = f"⚡ [TaskFlow Alert] Human Review Required #{item.review_id}"
    draft_preview = item.draft.response_text[:300] if item.draft else "No draft generated"
    body = f"""TaskFlow Human Review Alert
----------------------------
Review ID:    {item.review_id}
Trace ID:     {item.trace_id}
Tenant ID:    {item.tenant_id}
Reason:       {item.decision.reason}
Reason Code:  {item.decision.reason_code}
Created At:   {item.created_at}

Generated Draft Response:
{draft_preview}

Action: Open the TaskFlow Operator Dashboard to review, edit, or approve.
"""
    results = {}
    results["email"] = await send_email_alert(subject, body)
    results["telegram"] = await send_telegram_alert(
        f"⚡ *TaskFlow Alert*\nReview #{item.review_id}\nReason: {item.decision.reason}"
    )
    results["slack"] = await send_slack_alert(
        f"⚡ *TaskFlow Alert*: Review #{item.review_id} - {item.decision.reason}"
    )
    results["webhook"] = await send_custom_webhook_alert(item.model_dump(mode="json"))

    return results
