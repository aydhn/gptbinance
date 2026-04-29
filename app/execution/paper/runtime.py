"""Core runtime event loop orchestration."""
import logging
from typing import Dict, Any, Optional
import uuid

from .models import (
    PaperSessionConfig,
    PaperOrderIntent,
    PaperOrderStatus,
    SessionStopReason,
)
from .order_book import PaperOrderBook
from .fill_simulator import PaperFillSimulator
from .position_book import PositionBookManager
from .pnl import PnlTracker
from .intent_queue import IntentQueue
from .health import HealthMonitor
from .telemetry import RuntimeTelemetry
from .notifier_bridge import PaperNotifierBridge
from .storage import PaperStorage

logger = logging.getLogger(__name__)


class PaperRuntimeOrchestrator:
    def __init__(
        self,
        run_id: str,
        config: PaperSessionConfig,
        notifier_bridge: PaperNotifierBridge,
        storage: PaperStorage,
    ):
        self.run_id = run_id
        self.config = config
        self.notifier = notifier_bridge
        self.storage = storage

        self.order_book = PaperOrderBook()
        self.fill_sim = PaperFillSimulator(
            trigger=config.fill_trigger,
            max_slippage_pct=config.max_slippage_pct,
            maker_fee_pct=config.maker_fee_pct,
            taker_fee_pct=config.taker_fee_pct,
        )
        self.position_book = PositionBookManager()
        self.pnl_tracker = PnlTracker(initial_capital=config.initial_capital)
        self.intent_queue = IntentQueue()
        self.health = HealthMonitor()
        self.telemetry = RuntimeTelemetry()

        self.current_prices: Dict[str, float] = {}

    def handle_market_event(
        self, symbol: str, price: float, is_closed_bar: bool, event_time_ms: int
    ):
        """Main event loop hook for incoming market data."""
        self.current_prices[symbol] = price
        self.health.record_stream_event(symbol, event_time_ms)

        # In a full implementation:
        # 1. Update state cache (features)
        # 2. Trigger strategy evaluation -> Strategy generates Intent
        # 3. Apply regime context
        # 4. Risk engine evaluates Intent
        # 5. If approved, enqueue to intent_queue

        # Here we simulate processing the queue
        self._process_queue()

        # 6. Fill Simulation
        open_orders = self.order_book.get_open_orders(symbol)
        if open_orders:
            fills = self.fill_sim.evaluate(open_orders, price, is_closed_bar)
            for fill in fills:
                self._process_fill(fill)

        # 7. Snapshot PnL and Health periodically or per event
        eq_snap = self.pnl_tracker.get_snapshot(self.position_book, self.current_prices)
        open_pos_count = len([p for p in self.position_book.get_all() if p.qty != 0])
        health_snap = self.health.get_snapshot(eq_snap.drawdown_pct, open_pos_count)

        # Save snapshot
        self.storage.save_snapshot(self.run_id, eq_snap, health_snap)

        # Notifications
        if eq_snap.drawdown_pct > 0.05:
            self.notifier.notify_drawdown_warning(self.run_id, eq_snap.drawdown_pct)

    def _process_queue(self):
        intents = self.intent_queue.dequeue_all()
        for intent in intents:
            try:
                order_id = f"ord_{uuid.uuid4().hex[:8]}"
                order = self.order_book.add_from_intent(intent, order_id)
                self.telemetry.inc_order()

                # Assume immediate acceptance for now
                self.order_book.update_status(order_id, PaperOrderStatus.ACCEPTED)
                self.storage.save_order(self.run_id, order)

            except Exception as e:
                self.health.record_error(
                    f"Failed to process intent {intent.intent_id}: {str(e)}"
                )

    def _process_fill(self, fill):
        self.telemetry.inc_fill()
        order = self.order_book.update_status(
            fill.order_id,
            PaperOrderStatus.FILLED,
            fill_price=fill.price,
            fees=fill.fees,
            fill_assumption=self.config.fill_trigger.value,
        )
        self.storage.save_order(self.run_id, order)
        self.storage.save_fill(self.run_id, fill)

        realized_pnl = self.position_book.process_fill(fill)
        self.pnl_tracker.add_realized_pnl(realized_pnl)
        self.pnl_tracker.add_fee(fill.fees)

        self.notifier.notify_fill(
            self.run_id, fill.symbol, fill.side, fill.qty, fill.price, realized_pnl
        )

    def enqueue_intent(self, intent: PaperOrderIntent):
        """Exposed for strategy/risk to inject intents."""
        if self.intent_queue.enqueue(intent):
            self.telemetry.inc_intent()
