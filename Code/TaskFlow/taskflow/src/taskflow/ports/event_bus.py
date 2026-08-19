from collections.abc import AsyncIterator
from typing import Protocol

from pydantic import BaseModel

from taskflow.domain.models import InboundMessage


class Delivery(BaseModel):
    delivery_id: str
    message: InboundMessage
    attempt: int = 1


class EventBus(Protocol):
    async def publish(self, message: InboundMessage) -> str: ...
    def consume(self, consumer: str) -> AsyncIterator[Delivery]: ...
    async def ack(self, delivery: Delivery) -> None: ...
    async def dead_letter(self, delivery: Delivery, reason: str) -> None: ...
    async def pending_count(self) -> int: ...
    async def health(self) -> bool: ...
