"""PnL tracking for paper runtime."""

import logging
from .models import PaperEquitySnapshot
from .position_book import PositionBookManager

logger = logging.getLogger(__name__)


class PnlTracker:
    def __init__(self, initial_capital: float):
        self.initial_capital = initial_capital
        self.current_equity = initial_capital
        self.peak_equity = initial_capital
        self.total_fees = 0.0
        self.total_realized_pnl = 0.0

    def add_fee(self, fee: float):
        self.total_fees += fee
        self.current_equity -= fee

    def add_realized_pnl(self, amount: float):
        self.total_realized_pnl += amount
        self.current_equity += amount
        if self.current_equity > self.peak_equity:
            self.peak_equity = self.current_equity

    def get_snapshot(
        self, position_book: PositionBookManager, current_prices: dict[str, float]
    ) -> PaperEquitySnapshot:
        unrealized_pnl = 0.0
        for pos in position_book.get_all():
            if pos.qty != 0 and pos.symbol in current_prices:
                mark_price = current_prices[pos.symbol]
                if pos.qty > 0:
                    unrealized_pnl += pos.qty * (mark_price - pos.avg_entry_price)
                else:
                    unrealized_pnl += abs(pos.qty) * (pos.avg_entry_price - mark_price)

        total_equity = self.current_equity + unrealized_pnl

        peak = max(self.peak_equity, total_equity)
        self.peak_equity = peak

        drawdown_pct = 0.0
        if peak > 0:
            drawdown_pct = (peak - total_equity) / peak

        return PaperEquitySnapshot(equity=total_equity, drawdown_pct=drawdown_pct)
