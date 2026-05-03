from typing import Dict, Any
from app.events.models import EventRiskOverlay
from app.events.enums import EventGateVerdict


def adjust_portfolio_for_event(
    allocation: Dict[str, Any], overlay: EventRiskOverlay
) -> Dict[str, Any]:
    adjusted = allocation.copy()
    if overlay.verdict in [EventGateVerdict.REDUCE_ONLY, EventGateVerdict.REDUCE]:
        if "budget" in adjusted:
            adjusted["budget"] *= 0.5
            adjusted["_event_adjusted"] = True
            adjusted["_event_reasons"] = overlay.reasons
    elif overlay.verdict in [EventGateVerdict.BLOCK, EventGateVerdict.HALT]:
        if "budget" in adjusted:
            adjusted["budget"] = 0.0
            adjusted["_event_adjusted"] = True
            adjusted["_event_reasons"] = overlay.reasons
    return adjusted
