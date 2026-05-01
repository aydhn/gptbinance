from typing import Any
from app.analytics.base import AttributionAnalyzerBase
from app.analytics.models import AnalyticsRun, PortfolioAttributionRow


class PortfolioAttributionAnalyzer(AttributionAnalyzerBase):
    def analyze(self, run: AnalyticsRun, data: Any) -> PortfolioAttributionRow:
        # Expected data: portfolio repository summary or similar structure containing
        # counts of approved, reduced, deferred, rejected and stats about concentration.

        # Mock logic
        app = (
            data.get("total_approved", 0)
            if isinstance(data, dict)
            else getattr(data, "total_approved", 0)
        )
        red = (
            data.get("total_reduced", 0)
            if isinstance(data, dict)
            else getattr(data, "total_reduced", 0)
        )
        def_ = (
            data.get("total_deferred", 0)
            if isinstance(data, dict)
            else getattr(data, "total_deferred", 0)
        )
        rej = (
            data.get("total_rejected", 0)
            if isinstance(data, dict)
            else getattr(data, "total_rejected", 0)
        )

        return PortfolioAttributionRow(
            ranking_impact=0.0,  # Real logic needs full opportunity cost analysis
            concentration_impact=0.0,
            reserve_cash_opportunity_cost=0.0,
            total_approved=app,
            total_reduced=red,
            total_deferred=def_,
            total_rejected=rej,
        )
