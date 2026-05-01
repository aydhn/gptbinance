from datetime import datetime
from typing import List
from app.analytics.models import SessionAnalyticsSummary, PeriodAnalyticsSummary
from app.analytics.enums import PeriodGranularity


class PeriodicSummaryGenerator:
    def generate_session_summary(
        self,
        run_id: str,
        pnl: float,
        strategy_attr,
        regime_attr,
        port_attr,
        exec_qual,
        anomalies,
        divergence,
        diagnostics,
    ) -> SessionAnalyticsSummary:
        return SessionAnalyticsSummary(
            run_id=run_id,
            total_pnl=pnl,
            strategy_attribution=strategy_attr,
            regime_attribution=regime_attr,
            portfolio_attribution=port_attr,
            execution_quality=exec_qual,
            anomalies=anomalies,
            divergence_warnings=divergence,
            diagnostics=diagnostics,
        )

    def aggregate_periods(
        self,
        granularity: PeriodGranularity,
        start: datetime,
        end: datetime,
        sessions: List[SessionAnalyticsSummary],
    ) -> PeriodAnalyticsSummary:
        total_pnl = sum(s.total_pnl for s in sessions)
        return PeriodAnalyticsSummary(
            granularity=granularity,
            start_time=start,
            end_time=end,
            total_pnl=total_pnl,
            session_summaries=sessions,
        )
