from typing import Dict, List, Optional
from .models import TelemetryGapFinding

class GapDetectorRegistry:
    def __init__(self):
        self._gaps: Dict[str, TelemetryGapFinding] = {}

    def report_gap(self, gap: TelemetryGapFinding) -> None:
        self._gaps[gap.gap_id] = gap

    def get_gap(self, gap_id: str) -> Optional[TelemetryGapFinding]:
        return self._gaps.get(gap_id)

    def list_gaps(self) -> List[TelemetryGapFinding]:
        return list(self._gaps.values())
