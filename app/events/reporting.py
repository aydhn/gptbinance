from typing import List
from app.events.models import EventRecord, EventRiskOverlay, EventBlackoutWindow
from app.events.enums import EventSeverity


def generate_upcoming_events_report(events: List[EventRecord]) -> str:
    lines = ["=== UPCOMING HIGH IMPACT EVENTS ==="]
    high_impact = [
        e for e in events if e.severity in (EventSeverity.HIGH, EventSeverity.CRITICAL)
    ]
    if not high_impact:
        lines.append("No high impact events approaching.")
    else:
        for e in high_impact:
            lines.append(f"[{e.timestamp}] {e.title} (Severity: {e.severity.value})")
    return "\n".join(lines)


def generate_overlay_summary(overlay: EventRiskOverlay) -> str:
    lines = ["=== EVENT RISK OVERLAY ==="]
    lines.append(f"Verdict: {overlay.verdict.value}")
    lines.append("Reasons:")
    for r in overlay.reasons:
        lines.append(f" - {r}")
    return "\n".join(lines)


def generate_blackout_summary(blackouts: List[EventBlackoutWindow]) -> str:
    lines = ["=== ACTIVE BLACKOUTS ==="]
    if not blackouts:
        lines.append("No active blackouts.")
    else:
        for b in blackouts:
            lines.append(
                f"[{b.start_time} - {b.end_time}] {b.blackout_type.value}: {b.reason}"
            )
    return "\n".join(lines)
