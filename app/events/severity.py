from app.events.enums import EventSeverity, EventCategory


def adjust_severity(
    base_severity: EventSeverity, profile_id: str, category: EventCategory
) -> EventSeverity:
    if profile_id == "canary_live_caution":
        if base_severity == EventSeverity.HIGH:
            return EventSeverity.CRITICAL
    return base_severity
