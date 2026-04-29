from app.execution.live_runtime.models import (
    LiveCapitalCaps,
    LiveRuntimeDecision,
    LiveSessionState,
    LivePositionBook,
    LivePnlSnapshot,
)
from app.execution.live_runtime.enums import LiveRuntimeVerdict, CapitalCapType
from typing import Dict, Any, List


class CapitalCapEnforcer:
    def __init__(self, caps: LiveCapitalCaps):
        self.caps = caps
        self.session_orders = 0
        self.session_notional = 0.0

    def evaluate_intent(
        self, intent: Dict[str, Any], position_book: LivePositionBook
    ) -> LiveRuntimeDecision:
        symbol = intent.get("symbol", "")
        qty = intent.get("qty", 0.0)
        price = intent.get("price", 0.0)
        notional = qty * price

        allowed_symbols = [al.symbol for al in self.caps.allowlist]
        if symbol not in allowed_symbols:
            return LiveRuntimeDecision(
                verdict=LiveRuntimeVerdict.REJECT,
                reason=f"Symbol {symbol} is not in capital cap allowlist.",
                cap_type=CapitalCapType.MAX_SYMBOL_NOTIONAL,
            )

        allowance = next(
            (al for al in self.caps.allowlist if al.symbol == symbol), None
        )

        if allowance and notional > allowance.max_notional_usd:
            return LiveRuntimeDecision(
                verdict=LiveRuntimeVerdict.REJECT,
                reason=f"Notional {notional} exceeds symbol cap {allowance.max_notional_usd}.",
                cap_type=CapitalCapType.MAX_SYMBOL_NOTIONAL,
            )

        if self.session_notional + notional > self.caps.max_session_notional_usd:
            return LiveRuntimeDecision(
                verdict=LiveRuntimeVerdict.REJECT,
                reason=f"Notional {notional} would exceed session max {self.caps.max_session_notional_usd}.",
                cap_type=CapitalCapType.MAX_SESSION_NOTIONAL,
            )

        if self.session_orders + 1 > self.caps.max_new_orders_per_session:
            return LiveRuntimeDecision(
                verdict=LiveRuntimeVerdict.REJECT,
                reason=f"Order count would exceed session max {self.caps.max_new_orders_per_session}.",
                cap_type=CapitalCapType.MAX_NEW_ORDERS,
            )

        # Live exposure
        current_exposure = sum(
            [p.qty * p.avg_entry_price for p in position_book.positions.values()]
        )
        if current_exposure + notional > self.caps.max_live_exposure_usd:
            return LiveRuntimeDecision(
                verdict=LiveRuntimeVerdict.REJECT,
                reason=f"Notional would exceed max live exposure {self.caps.max_live_exposure_usd}.",
                cap_type=CapitalCapType.MAX_LIVE_EXPOSURE,
            )

        return LiveRuntimeDecision(
            verdict=LiveRuntimeVerdict.PROCEED, reason="Capital caps ok."
        )

    def record_submit(self, notional: float):
        self.session_orders += 1
        self.session_notional += notional

    def evaluate_loss(self, pnl: List[LivePnlSnapshot]) -> LiveRuntimeDecision:
        total_loss = 0.0
        for p in pnl:
            total_loss += p.realized_pnl + p.unrealized_pnl

        if total_loss < 0 and abs(total_loss) > self.caps.max_daily_loss_usd:
            return LiveRuntimeDecision(
                verdict=LiveRuntimeVerdict.HALT,
                reason=f"Loss {abs(total_loss)} exceeds max daily loss {self.caps.max_daily_loss_usd}.",
                cap_type=CapitalCapType.MAX_DAILY_LOSS,
            )
        return LiveRuntimeDecision(
            verdict=LiveRuntimeVerdict.PROCEED, reason="Loss within limits."
        )
