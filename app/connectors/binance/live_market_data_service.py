import asyncio
import logging
from typing import List, Callable, Awaitable, Optional

from app.config.models import AppConfig
from app.data.event_bus import EventBus
from app.data.live_stream_base import BaseLiveStreamManager, StreamCallback
from app.data.live_stream_models import (
    BookTickerEvent,
    KlineUpdateEvent,
    ReconnectEvent,
    StreamErrorEvent,
    StreamHealthSnapshot,
    StreamStatusEvent,
    SubscriptionSpec,
    TickerEvent,
)
from app.data.state_cache import StateCache
from app.data.stream_buffer import StreamBuffer

from .subscription_registry import SubscriptionRegistry
from .ws_client import BinanceWsClient
from .ws_health import WsHealthMonitor
from .ws_message_parser import BinanceWsMessageParser

logger = logging.getLogger(__name__)


class LiveMarketDataService(BaseLiveStreamManager):
    """
    Cohesive API for live market data. Coordinates WS client, parser, health,
    registry, cache, buffer, and event bus.
    """

    def __init__(
        self,
        config: AppConfig,
        event_bus: EventBus,
        state_cache: StateCache,
        stream_buffer: StreamBuffer,
    ):
        self.config = config
        self.event_bus = event_bus
        self.state_cache = state_cache
        self.stream_buffer = stream_buffer

        self.parser = BinanceWsMessageParser()
        self.health = WsHealthMonitor()
        self.registry = SubscriptionRegistry()

        self._callback: Optional[StreamCallback] = None

        # The base URL for combined streams
        self.base_url = "wss://stream.binance.com:9443/stream"
        if config.binance.testnet:
            self.base_url = "wss://testnet.binance.vision/stream"

        self.ws_client = BinanceWsClient(
            base_url=self.base_url,
            on_message_cb=self._on_message,
            on_connect_cb=self._on_connect,
            on_disconnect_cb=self._on_disconnect,
        )

        # Keep track of active task for health checking
        self._health_task: asyncio.Task | None = None

    def set_callback(self, callback: StreamCallback) -> None:
        """Register the callback to bypass event_bus latency for paper runtime."""
        self._callback = callback

    async def start(self) -> None:
        """Starts the websocket client and health monitoring."""
        await self.ws_client.start()
        self._health_task = asyncio.create_task(self._health_check_loop())

    async def stop(self) -> None:
        """Stops the websocket client and health monitoring."""
        if self._health_task:
            self._health_task.cancel()
        await self.ws_client.stop()

    async def subscribe(self, specs: List[SubscriptionSpec]) -> None:
        """Adds new subscriptions."""
        new_streams = self.registry.add_subscriptions(specs)
        if new_streams:
            await self._update_subscriptions("SUBSCRIBE", new_streams)

    async def unsubscribe(self, specs: List[SubscriptionSpec]) -> None:
        """Removes subscriptions."""
        removed_streams = self.registry.remove_subscriptions(specs)
        if removed_streams:
            await self._update_subscriptions("UNSUBSCRIBE", removed_streams)

    def get_health(self) -> StreamHealthSnapshot:
        return self.health.get_health_snapshot()

    async def _update_subscriptions(self, method: str, streams: List[str]) -> None:
        """Sends a subscribe/unsubscribe payload to the WS."""
        payload = {
            "method": method,
            "params": streams,
            "id": 1,  # Can be generated sequence ID later
        }
        await self.ws_client.send(payload)

    async def _on_connect(self) -> None:
        self.health.mark_connected()
        await self.event_bus.publish(StreamStatusEvent(status="connected"))
        # Resubscribe to active streams if any (on reconnect)
        active_streams = self.registry.get_active_streams()
        if active_streams:
            logger.info(
                f"Resubscribing to {len(active_streams)} streams after connect."
            )
            await self._update_subscriptions("SUBSCRIBE", active_streams)

    async def _on_disconnect(self, reason: str) -> None:
        self.health.mark_disconnected()
        self.health.increment_reconnect()

        await self.event_bus.publish(
            StreamStatusEvent(status="disconnected", reason=reason)
        )

        snapshot = self.health.get_health_snapshot()
        await self.event_bus.publish(
            ReconnectEvent(attempt=snapshot.reconnect_count, reason=reason)
        )

    async def _on_message(self, raw_message: str) -> None:
        self.health.record_message_received()

        event = self.parser.parse_message(raw_message)
        if not event:
            self.health.record_error("Failed to parse message")
            # Might be a simple subscription confirmation, so we don't always want to spam errors
            if "result" not in raw_message:
                await self.event_bus.publish(
                    StreamErrorEvent(
                        error_type="parse_error",
                        message="Could not parse websocket message",
                        raw_payload=raw_message,
                    )
                )
            return

        self.health.record_parse_success()

        # Buffer it
        self.stream_buffer.add_event(event)

        # Cache update and Publish
        price = 0.0
        is_closed = False
        symbol = event.symbol

        if isinstance(event, KlineUpdateEvent):
            self.state_cache.update_kline(event)
            price = event.close_price
            is_closed = event.is_closed
        elif isinstance(event, TickerEvent):
            self.state_cache.update_ticker(event)
            price = event.last_price
        elif isinstance(event, BookTickerEvent):
            self.state_cache.update_book_ticker(event)
            # Mid price approx
            price = (event.best_bid_price + event.best_ask_price) / 2

        # Fast path for paper runtime using callback
        if self._callback and price > 0.0:
            try:
                await self._callback(symbol, price, is_closed, event.event_time)
            except Exception as e:
                logger.error(f"Error in stream callback: {e}")

        await self.event_bus.publish(event)

    async def _health_check_loop(self) -> None:
        while True:
            await asyncio.sleep(10)
            if self.health.is_stale():
                logger.warning("Stream detected as stale.")
                await self.event_bus.publish(
                    StreamStatusEvent(status="degraded", reason="stale_stream")
                )
