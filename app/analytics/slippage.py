from typing import List, Any
from app.analytics.base import AttributionAnalyzerBase
from app.analytics.models import AnalyticsRun, SlippageReport


class SlippageAnalyzer(AttributionAnalyzerBase):
    def analyze(self, run: AnalyticsRun, data: List[Any]) -> SlippageReport:
        # Mock logic
        entry_slip = 1.5
        exit_slip = 1.8

        return SlippageReport(
            run_id=run.run_id,
            avg_entry_slippage_bps=entry_slip,
            avg_exit_slippage_bps=exit_slip,
            symbol_slippage={"BTCUSDT": 1.65},
        )
