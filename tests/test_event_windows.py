
from datetime import datetime, timezone, timedelta
from app.events.models import EventRecord
from app.events.enums import (
    EventCategory,
    EventSeverity,
    EventConfidence,
    EventFreshness,
)
from app.events.windows import calculate_window, merge_windows


def test_window_calculation_and_merge():
    now = datetime.now(timezone.utc)
    e1 = EventRecord(
        event_id="1",
        source_id="src1",
        title="E1",
        category=EventCategory.OTHER,
        severity=EventSeverity.HIGH,
        confidence=EventConfidence.HIGH,
        timestamp=now,
        freshness=EventFreshness.FRESH,
    )
    e2 = EventRecord(
        event_id="2",
        source_id="src1",
        title="E2",
        category=EventCategory.OTHER,
        severity=EventSeverity.MEDIUM,
        confidence=EventConfidence.HIGH,
        timestamp=now + timedelta(minutes=10),
        freshness=EventFreshness.FRESH,
    )
    w1 = calculate_window(e1, pre_minutes=30, post_minutes=30)
    w2 = calculate_window(e2, pre_minutes=30, post_minutes=30)

    merged = merge_windows([w1, w2])
    assert len(merged) == 1
    assert merged[0].max_severity == EventSeverity.HIGH
    assert merged[0].start_time == w1.start_time
    assert merged[0].end_time == w2.end_time
