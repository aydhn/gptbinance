
from datetime import datetime, timezone
from app.events.models import EventRecord
from app.events.enums import (
    EventCategory,
    EventSeverity,
    EventConfidence,
    EventFreshness,
    EventGateVerdict,
)
from app.events.overlay import DefaultOverlayEngine


def test_overlay_generation():
    engine = DefaultOverlayEngine()
    now = datetime.now(timezone.utc)
    e1 = EventRecord(
        event_id="1",
        source_id="src1",
        title="E1",
        category=EventCategory.OTHER,
        severity=EventSeverity.CRITICAL,
        confidence=EventConfidence.HIGH,
        timestamp=now,
        freshness=EventFreshness.FRESH,
    )
    overlay = engine.generate_overlay([e1], "default")
    assert overlay.verdict == EventGateVerdict.BLOCK
