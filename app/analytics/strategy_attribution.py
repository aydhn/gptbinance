from typing import List
from app.analytics.base import AttributionAnalyzerBase
from app.analytics.models import (
    AnalyticsRun,
    StrategyAttributionRow,
    TradeLifecycleSummary,
)


class StrategyAttributionAnalyzer(AttributionAnalyzerBase):
    def analyze(
        self, run: AnalyticsRun, data: List[TradeLifecycleSummary]
    ) -> List[StrategyAttributionRow]:
        family_stats = {}

        for trade in data:
            f = trade.strategy_family
            if f not in family_stats:
                family_stats[f] = {
                    "count": 0,
                    "pnl": 0.0,
                    "wins": 0,
                    "fees": 0.0,
                    "dd_contrib": 0.0,
                }

            family_stats[f]["count"] += 1
            family_stats[f]["pnl"] += trade.pnl
            family_stats[f]["fees"] += trade.fees
            if trade.pnl > 0:
                family_stats[f]["wins"] += 1

        results = []
        for f, s in family_stats.items():
            count = s["count"]
            hit_rate = s["wins"] / count if count > 0 else 0.0
            expectancy = s["pnl"] / count if count > 0 else 0.0

            row = StrategyAttributionRow(
                strategy_family=f,
                trade_count=count,
                pnl=s["pnl"],
                expectancy=expectancy,
                hit_rate=hit_rate,
                drawdown_contribution=s[
                    "dd_contrib"
                ],  # Needs deeper timeseries logic for real dd_contrib
                cost_burden=s["fees"],
            )
            results.append(row)

        return results
