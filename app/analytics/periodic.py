from datetime import datetime, timezone
from typing import List, Optional, Any
from app.analytics.models import SessionSummary, PeriodicAggregation
from app.analytics.enums import PeriodGranularity


class PeriodicSummaryGenerator:
    def generate_session_summary(
        self,
        run_id: str,
        net_pnl: float,
        trades: List,
        signals: List,
        risk: Optional[Any],
        performance: Optional[Any],
        ml: List,
        errors: List,
        audits: List,
    ) -> SessionSummary:
        return SessionSummary(
            run_id=run_id,
            timestamp=datetime.now(timezone.utc),
            net_pnl=net_pnl,
            trade_count=len(trades),
            signal_count=len(signals),
            error_count=len(errors),
        )

    def aggregate_periods(
        self,
        granularity: PeriodGranularity,
        start_time: datetime,
        end_time: datetime,
        summaries: List[SessionSummary],
    ) -> PeriodicAggregation:

        total_pnl = sum(s.net_pnl for s in summaries)
        return PeriodicAggregation(
            granularity=granularity,
            start_time=start_time,
            end_time=end_time,
            total_pnl=total_pnl,
            session_summaries=summaries,
        )


def generate_daily_summary():
    pass
