from datetime import datetime
from typing import Protocol

from pydantic import BaseModel

from taskflow.domain.enums import Channel
from taskflow.domain.models import InboundMessage, OutboundMessage


class DeliveryReceipt(BaseModel):
    provider_message_id: str
    delivered_at: datetime


class ChannelConnector(Protocol):
    """Poll or push, email or chat — the pipeline never knows which."""

    channel: Channel

    async def fetch(self) -> list[InboundMessage]: ...
    async def send(self, outbound: OutboundMessage) -> DeliveryReceipt: ...
    async def health(self) -> bool: ...
