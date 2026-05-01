from typing import List, Any
from app.analytics.base import AttributionAnalyzerBase
from app.analytics.models import AnalyticsRun, ExecutionQualityReport
from app.analytics.enums import ExecutionQualityVerdict, JournalEventType


class ExecutionQualityAnalyzer(AttributionAnalyzerBase):
    def analyze(self, run: AnalyticsRun, data: List[Any]) -> ExecutionQualityReport:
        # data expected to be trade journal entries filtered to execution scope
        submit = sum(
            1
            for e in data
            if getattr(e, "event_type", None) == JournalEventType.ORDER_SUBMITTED
        )
        fill = sum(
            1
            for e in data
            if getattr(e, "event_type", None) == JournalEventType.ORDER_FILLED
        )
        rej = sum(
            1
            for e in data
            if getattr(e, "event_type", None) == JournalEventType.ORDER_REJECTED
        )
        canc = sum(
            1
            for e in data
            if getattr(e, "event_type", None) == JournalEventType.ORDER_CANCELLED
        )

        # Latency logic mocked
        avg_ack = 50.0
        avg_fill = 150.0

        partial_rate = 0.0  # Placeholder

        verdict = ExecutionQualityVerdict.GOOD
        if rej > submit * 0.1:
            verdict = ExecutionQualityVerdict.DEGRADED

        return ExecutionQualityReport(
            run_id=run.run_id,
            verdict=verdict,
            submit_count=submit,
            fill_count=fill,
            reject_count=rej,
            cancel_count=canc,
            avg_ack_latency_ms=avg_ack,
            avg_fill_latency_ms=avg_fill,
            partial_fill_rate=partial_rate,
        )
