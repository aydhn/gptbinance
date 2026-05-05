from app.market_truth.models import GapFinding, GapCluster
from app.market_truth.enums import GapType
from typing import List


class GapDetector:
    def detect_gaps(self, sequence_ids: List[int]) -> GapCluster:
        findings = []
        for i in range(1, len(sequence_ids)):
            expected = sequence_ids[i - 1] + 1
            if sequence_ids[i] > expected:
                diff = sequence_ids[i] - sequence_ids[i - 1] - 1
                gap_type = GapType.TRANSIENT_GAP if diff < 5 else GapType.PERSISTENT_GAP
                findings.append(
                    GapFinding(
                        gap_type=gap_type,
                        start_id=sequence_ids[i - 1],
                        end_id=sequence_ids[i],
                        missing_count=diff,
                        severity="HIGH"
                        if gap_type == GapType.PERSISTENT_GAP
                        else "MEDIUM",
                    )
                )
        return GapCluster(findings=findings)
