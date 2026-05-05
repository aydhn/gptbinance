from app.market_truth.base import SequenceCheckerBase
from app.market_truth.models import SequenceIntegrityReport, GapCluster
from app.market_truth.enums import StreamType
from typing import List


class SequenceIntegrityEngine(SequenceCheckerBase):
    def check_integrity(self, events: List[dict]) -> SequenceIntegrityReport:
        # Expect events to have 'u' or 'U' for update ids if depth, or sequence logic
        is_monotonic = True
        for i in range(1, len(events)):
            if events[i].get("id", 0) <= events[i - 1].get("id", 0):
                is_monotonic = False
                break

        return SequenceIntegrityReport(
            stream_type=StreamType.TRADE,
            symbol="UNKNOWN",
            is_monotonic=is_monotonic,
            gaps=GapCluster(findings=[]),
        )
