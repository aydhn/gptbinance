from app.events.models import EventRiskOverlay
from app.events.enums import EventGateVerdict
from typing import List, Tuple


def validate_execution_against_events(
    overlay: EventRiskOverlay, is_entry: bool = True
) -> Tuple[bool, List[str]]:
    if overlay.verdict == EventGateVerdict.HALT:
        return False, ["Execution halted due to critical event/maintenance."]

    if overlay.verdict == EventGateVerdict.BLOCK and is_entry:
        return False, ["New entries blocked due to event overlay."]

    if overlay.verdict == EventGateVerdict.EXIT_ONLY and is_entry:
        return False, ["Only exits are allowed in current event window."]

    if overlay.verdict == EventGateVerdict.REDUCE_ONLY and is_entry:
        return False, ["Only reducing positions is allowed."]

    return True, []
