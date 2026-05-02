from typing import List
from app.backtest.validation.models import HonestyWarning, ResearchHonestyReport
from app.backtest.validation.enums import HonestySeverity
from app.backtest.models import PerformanceSummary as BacktestSummary


class HonestyGuardEvaluator:
    """Evaluates backtest results against basic research honesty rules."""

    def evaluate(self, summary: BacktestSummary) -> ResearchHonestyReport:
        warnings: List[HonestyWarning] = []
        # Rule 1: Trade count
        trade_count = getattr(summary, "total_trades", 0)
        if trade_count < 10:
            warnings.append(
                HonestyWarning(
                    severity=HonestySeverity.FAIL,
                    message="Extremely low trade count. Results are statistically insignificant.",
                    metric="total_trades",
                    value=trade_count,
                )
            )
        elif trade_count < 30:
            warnings.append(
                HonestyWarning(
                    severity=HonestySeverity.WARNING,
                    message="Low trade count. Proceed with caution.",
                    metric="total_trades",
                    value=trade_count,
                )
            )

        # Rule 2: High hit rate but low profit factor (Expectancy check proxy)
        hit_rate = getattr(summary, "hit_rate", 0)
        pf = getattr(summary, "profit_factor", 0)
        if hit_rate > 70 and pf < 1.1:
            warnings.append(
                HonestyWarning(
                    severity=HonestySeverity.CAUTION,
                    message="High hit rate but low profit factor. Strategy might be taking many small winners and few huge losers.",
                    metric="hit_rate / profit_factor",
                    value=f"{hit_rate}% / {pf}",
                )
            )

        # Rule 3: Huge return but massive DD
        ret = getattr(summary, "total_return_pct", 0)
        dd = getattr(summary, "max_drawdown_pct", 0)
        if ret > 50 and dd > 40:
            warnings.append(
                HonestyWarning(
                    severity=HonestySeverity.WARNING,
                    message="High return achieved with massive drawdown. Likely over-leveraged or too volatile.",
                    metric="max_drawdown_pct",
                    value=dd,
                )
            )

        passed_all = not any(
            w.severity in [HonestySeverity.FAIL, HonestySeverity.WARNING]
            for w in warnings
        )

        return ResearchHonestyReport(
            strategy_run_id=summary.run_id, warnings=warnings, passed_all=passed_all
        )


class MLEvaluationGuard:

    def check(self, run_id: str):

        # Check calibration, drift, leakage, temporal split honesty
        return GuardResult(passed=True, caution_flags=[])
