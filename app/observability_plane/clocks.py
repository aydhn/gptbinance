from typing import Dict, List, Optional
from .models import ClockSemanticRecord
from .exceptions import InvalidClockSemanticsError

class ClockSemanticsRegistry:
    def __init__(self):
        self._clocks: Dict[str, ClockSemanticRecord] = {}

    def register_clock(self, clock: ClockSemanticRecord) -> None:
        self._clocks[clock.telemetry_id] = clock

    def get_clock(self, telemetry_id: str) -> Optional[ClockSemanticRecord]:
        return self._clocks.get(telemetry_id)

    def assert_valid_clocks(self, telemetry_ids: List[str]) -> None:
        for tid in telemetry_ids:
            if tid not in self._clocks:
                raise InvalidClockSemanticsError(f"Missing clock semantics for {tid}")

    def list_clocks(self) -> List[ClockSemanticRecord]:
        return list(self._clocks.values())
