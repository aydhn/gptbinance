
from datetime import datetime, timezone
from app.events.portfolio import adjust_portfolio_for_event
from app.events.models import EventRiskOverlay
from app.events.enums import EventGateVerdict


def test_adjust_portfolio():
    overlay = EventRiskOverlay(
        overlay_id="o1",
        timestamp=datetime.now(timezone.utc),
        active_windows=[],
        verdict=EventGateVerdict.REDUCE_ONLY,
        reasons=["High impact event"],
    )
    alloc = {"budget": 1000.0}
    adjusted = adjust_portfolio_for_event(alloc, overlay)
    assert adjusted["budget"] == 500.0
    assert adjusted["_event_adjusted"] is True
