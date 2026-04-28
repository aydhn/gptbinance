from typing import List
from datetime import datetime
from app.backtest.models import EquitySnapshot, DrawdownSnapshot


class EquityTracker:
    def __init__(self, initial_capital: float):
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.high_water_mark = initial_capital
        self.snapshots: List[EquitySnapshot] = []

        self.current_drawdown_pct = 0.0
        self.max_drawdown_pct = 0.0
        self.max_drawdown_value = 0.0

    def process_fill(self, fee: float, realized_pnl: float):
        self.cash -= fee
        self.cash += realized_pnl

    def snapshot(self, timestamp: datetime, unrealized_pnl: float) -> EquitySnapshot:
        equity = self.cash + unrealized_pnl

        if equity > self.high_water_mark:
            self.high_water_mark = equity
            self.current_drawdown_pct = 0.0
        else:
            dd_value = self.high_water_mark - equity
            self.current_drawdown_pct = (
                (dd_value / self.high_water_mark) * 100.0
                if self.high_water_mark > 0
                else 0.0
            )

            if self.current_drawdown_pct > self.max_drawdown_pct:
                self.max_drawdown_pct = self.current_drawdown_pct
                self.max_drawdown_value = dd_value

        snap = EquitySnapshot(
            timestamp=timestamp,
            cash=self.cash,
            equity=equity,
            unrealized_pnl=unrealized_pnl,
            drawdown_pct=self.current_drawdown_pct,
            high_water_mark=self.high_water_mark,
        )
        self.snapshots.append(snap)
        return snap

    def get_drawdown_summary(self) -> DrawdownSnapshot:
        return DrawdownSnapshot(
            max_drawdown_pct=self.max_drawdown_pct,
            max_drawdown_value=self.max_drawdown_value,
            current_drawdown_pct=self.current_drawdown_pct,
        )
