from typing import List
from app.analytics.base import AttributionAnalyzerBase
from app.analytics.models import (
    AnalyticsRun,
    RegimeAttributionRow,
    TradeLifecycleSummary,
)


class RegimeAttributionAnalyzer(AttributionAnalyzerBase):
    def analyze(
        self, run: AnalyticsRun, data: List[TradeLifecycleSummary]
    ) -> List[RegimeAttributionRow]:
        regime_stats = {}

        for trade in data:
            r = trade.regime
            if r not in regime_stats:
                regime_stats[r] = {"count": 0, "pnl": 0.0, "expected_suitability": 1.0}

            regime_stats[r]["count"] += 1
            regime_stats[r]["pnl"] += trade.pnl

        results = []
        for r, s in regime_stats.items():
            # Suitability score is a mockup. In reality it would compare PnL to expected PnL for that regime.
            suitability = s["pnl"] / max(s["count"], 1)
            row = RegimeAttributionRow(
                regime=r,
                trade_count=s["count"],
                pnl=s["pnl"],
                suitability_score=suitability,
            )
            results.append(row)

        return results
