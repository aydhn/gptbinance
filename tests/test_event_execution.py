from datetime import datetime, timezone
from app.events.execution import validate_execution_against_events
from app.events.models import EventRiskOverlay
from app.events.enums import EventGateVerdict


def test_execution_validation():
    overlay = EventRiskOverlay(
        overlay_id="o1",
        timestamp=datetime.now(timezone.utc),
        active_windows=[],
        verdict=EventGateVerdict.BLOCK,
        reasons=["Critical event"],
    )
    valid, reasons = validate_execution_against_events(overlay, is_entry=True)
    assert not valid
    assert "blocked" in reasons[0]
