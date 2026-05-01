from typing import List, Any
from app.analytics.base import DivergenceAnalyzerBase
from app.analytics.models import (
    AnalyticsRun,
    DivergenceReport,
    LiveVsPaperComparison,
)
from app.analytics.enums import DivergenceType, AnomalySeverity, ComparisonVerdict


class DivergenceAnalyzer(DivergenceAnalyzerBase):
    def analyze(self, run: AnalyticsRun, data: Any) -> List[DivergenceReport]:
        reports = []

        # Example mocked report
        rep = DivergenceReport(
            run_id=run.run_id,
            type=DivergenceType.PAPER_VS_LIVE,
            severity=AnomalySeverity.LOW,
            evidence="Slight slippage deviation found.",
            likely_layer="Execution",
            recommended_checks=["Check fill latency", "Check order routing"],
            live_vs_paper=LiveVsPaperComparison(
                verdict=ComparisonVerdict.MINOR_DIVERGENCE,
                pnl_diff=-10.5,
                slippage_diff_bps=0.5,
                fill_rate_diff=-0.01,
            ),
        )
        reports.append(rep)
        return reports
