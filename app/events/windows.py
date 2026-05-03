from typing import List
from datetime import timedelta
from app.events.models import EventRecord, EventWindow
from app.events.enums import EventSeverity, CooldownMode


def calculate_window(
    event: EventRecord, pre_minutes: int = 30, post_minutes: int = 30
) -> EventWindow:
    start_time = event.timestamp - timedelta(minutes=pre_minutes)
    end_time = event.end_timestamp or event.timestamp + timedelta(minutes=post_minutes)

    return EventWindow(
        window_id=f"win_{event.event_id}",
        start_time=start_time,
        end_time=end_time,
        events=[event],
        max_severity=event.severity,
        cooldown_mode=CooldownMode.REDUCE_ONLY
        if event.severity in [EventSeverity.HIGH, EventSeverity.CRITICAL]
        else CooldownMode.NONE,
    )


def merge_windows(windows: List[EventWindow]) -> List[EventWindow]:
    if not windows:
        return []
    sorted_windows = sorted(windows, key=lambda w: w.start_time)
    merged = [sorted_windows[0]]
    for current in sorted_windows[1:]:
        last = merged[-1]
        if current.start_time <= last.end_time:
            last.end_time = max(last.end_time, current.end_time)
            last.events.extend(current.events)
            if (
                current.max_severity == EventSeverity.CRITICAL
                or last.max_severity == EventSeverity.CRITICAL
            ):
                last.max_severity = EventSeverity.CRITICAL
            elif (
                current.max_severity == EventSeverity.HIGH
                or last.max_severity == EventSeverity.HIGH
            ):
                last.max_severity = EventSeverity.HIGH
        else:
            merged.append(current)
    return merged
