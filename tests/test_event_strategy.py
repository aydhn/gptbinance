from datetime import datetime, timezone
from app.events.strategy import check_strategy_event_gate
from app.events.models import EventRiskOverlay
from app.events.enums import EventGateVerdict


def test_strategy_event_gate():
    overlay = EventRiskOverlay(
        overlay_id="o1",
        timestamp=datetime.now(timezone.utc),
        active_windows=[],
        verdict=EventGateVerdict.REDUCE_ONLY,
        reasons=["High impact"],
    )
    assert not check_strategy_event_gate({"event_sensitivity": "high"}, overlay)
    assert check_strategy_event_gate({"event_sensitivity": "low"}, overlay)
