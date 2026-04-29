from app.execution.live_runtime.models import (
    LivePositionBook,
    LivePnlSnapshot,
    LiveEquitySnapshot,
    LiveAccountSnapshot,
)
from typing import Dict
from datetime import datetime


class LivePnlCalculator:
    def __init__(self, run_id: str):
        self.run_id = run_id
        self.max_equity_seen = 0.0

    def compute_pnl(
        self, position_book: LivePositionBook, current_prices: Dict[str, float]
    ) -> list[LivePnlSnapshot]:
        snapshots = []
        for symbol, pos in position_book.positions.items():
            current_price = current_prices.get(symbol, pos.avg_entry_price)
            unrealized = 0.0
            if pos.qty != 0:
                unrealized = (current_price - pos.avg_entry_price) * pos.qty

            pos.unrealized_pnl = unrealized
            snapshots.append(
                LivePnlSnapshot(
                    symbol=symbol,
                    realized_pnl=pos.realized_pnl,
                    unrealized_pnl=unrealized,
                )
            )
        return snapshots

    def generate_equity_snapshot(
        self, base_account: LiveAccountSnapshot, pnl_snapshots: list[LivePnlSnapshot]
    ) -> LiveEquitySnapshot:
        base_usdt = 0.0
        for b in base_account.balances:
            if b.asset == "USDT":
                base_usdt = b.free + b.locked

        total_realized = sum(p.realized_pnl for p in pnl_snapshots)
        total_unrealized = sum(p.unrealized_pnl for p in pnl_snapshots)

        # Simplified: Initial equity + realized + unrealized
        current_equity = base_usdt + total_realized + total_unrealized

        if current_equity > self.max_equity_seen:
            self.max_equity_seen = current_equity

        drawdown_pct = 0.0
        if self.max_equity_seen > 0:
            drawdown_pct = (
                self.max_equity_seen - current_equity
            ) / self.max_equity_seen

        return LiveEquitySnapshot(
            run_id=self.run_id,
            total_equity_usd=current_equity,
            max_drawdown_pct=drawdown_pct,
            pnl_by_symbol=pnl_snapshots,
            timestamp=datetime.utcnow(),
        )
