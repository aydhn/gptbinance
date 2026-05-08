from typing import List
from .models import DataGapFinding, GapClass
from .exceptions import GapHandlingError


class GapDetector:
    def __init__(self):
        self._gaps: List[DataGapFinding] = []

    def detect_missing_bars(
        self, timestamps: List[float], interval_ms: int
    ) -> List[DataGapFinding]:
        findings = []
        if not timestamps:
            return findings

        timestamps.sort()
        for i in range(1, len(timestamps)):
            diff = timestamps[i] - timestamps[i - 1]
            if diff > interval_ms * 1.5:  # Tolerance for missing bar
                # Found a gap
                from datetime import datetime, timezone

                finding = DataGapFinding(
                    gap_id=f"gap_{timestamps[i-1]}_{timestamps[i]}",
                    gap_class=GapClass.MISSING_BAR,
                    start_time=datetime.fromtimestamp(
                        timestamps[i - 1] / 1000.0, tz=timezone.utc
                    ),
                    end_time=datetime.fromtimestamp(
                        timestamps[i] / 1000.0, tz=timezone.utc
                    ),
                )
                findings.append(finding)
                self._gaps.append(finding)
        return findings

    def list_gaps(self) -> List[DataGapFinding]:
        return self._gaps
