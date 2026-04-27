import asyncio
import logging
import json

from app.config.models import AppConfig
from app.data.event_bus import EventBus
from app.data.state_cache import StateCache
from app.data.stream_buffer import StreamBuffer
from app.data.live_stream_models import SubscriptionSpec, KlineUpdateEvent, TickerEvent
from app.connectors.binance.live_market_data_service import LiveMarketDataService
from app.core.enums import EnvironmentProfile

logger = logging.getLogger(__name__)


async def _run_smoke_test_async(
    config: AppConfig,
    profile: EnvironmentProfile,
    symbol: str,
    stream_type: str,
    seconds: int,
):
    logger.info(
        f"Starting live stream smoke test for {symbol} ({stream_type}) for {seconds}s"
    )

    event_bus = EventBus()
    state_cache = StateCache()
    stream_buffer = StreamBuffer()

    service = LiveMarketDataService(
        config=config,
        event_bus=event_bus,
        state_cache=state_cache,
        stream_buffer=stream_buffer,
    )

    # Handlers for logging
    async def log_kline(event: KlineUpdateEvent):
        logger.info(
            f"KLINE: {event.symbol} | Close: {event.close_price} | Closed: {event.is_closed}"
        )

    async def log_ticker(event: TickerEvent):
        logger.info(f"TICKER: {event.symbol} | Price: {event.last_price}")

    if stream_type == "kline":
        event_bus.subscribe(KlineUpdateEvent, log_kline)
        spec = SubscriptionSpec(symbol=symbol, stream_type="kline", interval="1m")
    elif stream_type == "ticker":
        event_bus.subscribe(TickerEvent, log_ticker)
        spec = SubscriptionSpec(symbol=symbol, stream_type="ticker")
    else:
        logger.error(f"Unsupported stream_type for smoke test: {stream_type}")
        return

    try:
        await service.start()
        await service.subscribe([spec])

        # Wait for the specified duration
        await asyncio.sleep(seconds)

        health = service.get_health()
        logger.info("=== STREAM HEALTH ===")
        logger.info(json.dumps(health.model_dump(), indent=2, default=str))

        cache_snap = state_cache.get_snapshot()
        logger.info("=== STATE CACHE SNAPSHOT ===")
        logger.info(json.dumps(cache_snap, indent=2, default=str))

        buffer_snap = stream_buffer.get_snapshot()
        logger.info("=== STREAM BUFFER EVENT COUNTS ===")
        logger.info(json.dumps(buffer_snap, indent=2))

    finally:
        logger.info("Stopping service...")
        await service.stop()
        logger.info("Smoke test complete.")


def run_live_stream_smoke(
    config: AppConfig,
    profile: EnvironmentProfile,
    symbol: str,
    stream_type: str,
    seconds: int,
):
    # Setup loop
    try:
        asyncio.run(
            _run_smoke_test_async(config, profile, symbol, stream_type, seconds)
        )
    except KeyboardInterrupt:
        logger.info("Smoke test interrupted by user.")
