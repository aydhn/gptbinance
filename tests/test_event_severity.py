from app.events.severity import adjust_severity
from app.events.enums import EventSeverity, EventCategory


def test_adjust_severity():
    assert (
        adjust_severity(
            EventSeverity.HIGH, "canary_live_caution", EventCategory.MACRO_POLICY
        )
        == EventSeverity.CRITICAL
    )
    assert (
        adjust_severity(EventSeverity.HIGH, "default", EventCategory.MACRO_POLICY)
        == EventSeverity.HIGH
    )
