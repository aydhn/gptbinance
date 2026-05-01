from datetime import datetime, timezone
from app.analytics.execution_quality import ExecutionQualityAnalyzer
from app.analytics.models import AnalyticsRun, AnalyticsConfig, TradeJournalEntry
from app.analytics.enums import (
    AnalyticsScope,
    JournalEventType,
    ExecutionQualityVerdict,
)


def test_execution_quality():
    run = AnalyticsRun(
        run_id="r1",
        config=AnalyticsConfig(scope=AnalyticsScope.SESSION),
        started_at=datetime.now(timezone.utc),
    )

    e1 = TradeJournalEntry(
        entry_id="1",
        run_id="r1",
        timestamp=datetime.now(timezone.utc),
        event_type=JournalEventType.ORDER_SUBMITTED,
        symbol="BTC",
    )
    e2 = TradeJournalEntry(
        entry_id="2",
        run_id="r1",
        timestamp=datetime.now(timezone.utc),
        event_type=JournalEventType.ORDER_FILLED,
        symbol="BTC",
    )
    e3 = TradeJournalEntry(
        entry_id="3",
        run_id="r1",
        timestamp=datetime.now(timezone.utc),
        event_type=JournalEventType.ORDER_SUBMITTED,
        symbol="BTC",
    )
    e4 = TradeJournalEntry(
        entry_id="4",
        run_id="r1",
        timestamp=datetime.now(timezone.utc),
        event_type=JournalEventType.ORDER_REJECTED,
        symbol="BTC",
    )

    analyzer = ExecutionQualityAnalyzer()
    res = analyzer.analyze(run, [e1, e2, e3, e4])

    assert res.submit_count == 2
    assert res.fill_count == 1
    assert res.reject_count == 1
    assert res.verdict == ExecutionQualityVerdict.DEGRADED
