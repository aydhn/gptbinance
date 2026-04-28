from typing import List
from app.backtest.models import (
    PerformanceSummary,
    TradeRecord,
    EquitySnapshot,
    DrawdownSnapshot,
)
from app.backtest.enums import TradeStatus


class PerformanceCalculator:
    @staticmethod
    def calculate(
        run_id: str,
        initial_capital: float,
        trades: List[TradeRecord],
        final_equity: float,
        drawdown_summary: DrawdownSnapshot,
        total_bars: int = 1,
    ) -> PerformanceSummary:
        completed_trades = [t for t in trades if t.status == TradeStatus.CLOSED]
        total_trades = len(completed_trades)

        total_return_pct = (
            ((final_equity - initial_capital) / initial_capital) * 100.0
            if initial_capital > 0
            else 0.0
        )

        winning_trades = [t for t in completed_trades if t.realized_pnl > 0]
        losing_trades = [t for t in completed_trades if t.realized_pnl <= 0]

        win_count = len(winning_trades)
        loss_count = len(losing_trades)

        hit_rate = (win_count / total_trades) * 100.0 if total_trades > 0 else 0.0

        gross_profit = sum(t.realized_pnl for t in winning_trades)
        gross_loss = abs(sum(t.realized_pnl for t in losing_trades))

        avg_win = gross_profit / win_count if win_count > 0 else 0.0
        avg_loss = gross_loss / loss_count if loss_count > 0 else 0.0

        profit_factor = (
            gross_profit / gross_loss
            if gross_loss > 0
            else (float("inf") if gross_profit > 0 else 0.0)
        )

        # Expectancy = (Hit Rate * Avg Win) - (Loss Rate * Avg Loss)
        win_rate_dec = win_count / total_trades if total_trades > 0 else 0.0
        loss_rate_dec = loss_count / total_trades if total_trades > 0 else 0.0
        expectancy = (win_rate_dec * avg_win) - (loss_rate_dec * avg_loss)

        total_fees = sum(t.total_fees for t in completed_trades)

        # Simple exposure ratio (just trades over total bars as a proxy for this simple version)
        exposure_ratio = total_trades / total_bars if total_bars > 0 else 0.0

        return PerformanceSummary(
            run_id=run_id,
            total_return_pct=total_return_pct,
            total_trades=total_trades,
            winning_trades=win_count,
            losing_trades=loss_count,
            hit_rate=hit_rate,
            average_win=avg_win,
            average_loss=avg_loss,
            expectancy=expectancy,
            profit_factor=profit_factor,
            max_drawdown_pct=drawdown_summary.max_drawdown_pct,
            exposure_ratio=exposure_ratio,
            total_fees_paid=total_fees,
            final_equity=final_equity,
            initial_capital=initial_capital,
        )
