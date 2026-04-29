import logging
from typing import Callable, Any, Optional
from app.execution.live.execution_parser import ExecutionParser
from app.execution.live.models import UserStreamEvent
from app.execution.live.enums import UserStreamEventType

logger = logging.getLogger(__name__)


class UserStreamManager:
    """Manages listen keys and parses incoming stream events."""

    def __init__(self, binance_client: Any):
        self.binance_client = binance_client
        self.listen_key: Optional[str] = None
        self.callbacks: list[Callable[[UserStreamEvent], None]] = []

    def register_callback(self, callback: Callable[[UserStreamEvent], None]):
        self.callbacks.append(callback)

    async def start(self):
        # Placeholder for actual listen key acquisition and websocket connection
        logger.info("Starting user stream manager")
        self.listen_key = "dummy_listen_key"

    async def keepalive(self):
        # Placeholder for keepalive logic
        pass

    def on_message(self, message: dict):
        event = ExecutionParser.parse_user_stream_event(message)
        if event:
            for cb in self.callbacks:
                cb(event)
