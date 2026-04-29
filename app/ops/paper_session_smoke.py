"""Short duration smoke test for paper session runtime."""
import asyncio
import logging
import uuid
from typing import Any

from app.config.models import AppConfig
from app.data.event_bus import EventBus
from app.data.state_cache import StateCache
from app.data.stream_buffer import StreamBuffer
from app.data.live_stream_models import SubscriptionSpec
from app.connectors.binance.live_market_data_service import LiveMarketDataService
from app.execution.paper.session import PaperSession
from app.execution.paper.models import PaperSessionConfig, FillTrigger

logger = logging.getLogger(__name__)


class SmokeTestCallback:
    def __init__(self, session: PaperSession):
        self.session = session
        self.counter = 0

    async def __call__(self, symbol: str, price: float, is_closed: bool, event_time_ms: int) -> None:
        # We process the event via the runtime hook
        self.session.runtime.handle_market_event(symbol, price, is_closed, event_time_ms)

        self.counter += 1

        if self.counter % 50 == 0:
            # Create intent
            from app.execution.paper.models import PaperOrderIntent

            intent = PaperOrderIntent(
                intent_id=f"intent_{uuid.uuid4().hex[:8]}",
                symbol=symbol,
                side="BUY" if self.counter % 100 == 0 else "SELL",
                qty=0.01,
                price=price,
            )
            self.session.runtime.enqueue_intent(intent)
            logger.info(
                f"Injected fake intent {intent.intent_id} for {symbol} at {price}"
            )


async def run_smoke_test(
    config: AppConfig, symbols: list[str], duration_seconds: int = 30
) -> None:
    logger.info(
        f"Starting Paper Session Smoke Test for {duration_seconds}s on {symbols}"
    )

    event_bus = EventBus()
    state_cache = StateCache()
    stream_buffer = StreamBuffer()

    stream_service = LiveMarketDataService(
        config=config,
        event_bus=event_bus,
        state_cache=state_cache,
        stream_buffer=stream_buffer,
    )

    paper_config = PaperSessionConfig(
        symbols=symbols,
        stream_types=["ticker"],
        duration_seconds=duration_seconds,
        fill_trigger=FillTrigger.NEXT_TICK,
        enable_telegram=False,
    )

    session = PaperSession(paper_config, config)

    callback = SmokeTestCallback(session)
    stream_service.set_callback(callback)

    # Start systems
    await stream_service.start()
    session.start()

    # Subscribe
    specs = [
        SubscriptionSpec(symbol=sym.lower(), stream_type="ticker") for sym in symbols
    ]
    await stream_service.subscribe(specs)

    # Wait
    await asyncio.sleep(duration_seconds)

    # Clean up
    await stream_service.unsubscribe(specs)
    await stream_service.stop()
    session.stop()

    logger.info("Smoke test complete. Check database for logs.")
