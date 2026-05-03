from typing import Dict, Any
from app.events.models import EventRiskOverlay
from app.events.enums import EventGateVerdict


def check_strategy_event_gate(
    strategy_metadata: Dict[str, Any], overlay: EventRiskOverlay
) -> bool:
    if overlay.verdict in [EventGateVerdict.BLOCK, EventGateVerdict.HALT]:
        return False

    event_sensitivity = strategy_metadata.get("event_sensitivity", "low")
    if overlay.verdict == EventGateVerdict.REDUCE_ONLY and event_sensitivity == "high":
        return False

    return True
