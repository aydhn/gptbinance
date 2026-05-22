from app.precedent_plane.models import PrecedentTrustVerdictReport
from app.precedent_plane.enums import PrecedentTrustVerdict
from typing import List

class TrustManager:
    def __init__(self):
        self.records: List[PrecedentTrustVerdictReport] = []

    def evaluate_trust(self, precedent_id: str, conflicts: List, holdings: List) -> PrecedentTrustVerdictReport:
        verdict = PrecedentTrustVerdict.TRUSTED
        breakdown = "Trusted based on clear holdings"

        if len(conflicts) > 0:
            verdict = PrecedentTrustVerdict.DEGRADED
            breakdown = "Degraded due to unresolved conflicts"

        if len(holdings) == 0:
            verdict = PrecedentTrustVerdict.REVIEW_REQUIRED
            breakdown = "Review required due to missing holdings"

        report = PrecedentTrustVerdictReport(
            precedent_id=precedent_id,
            verdict=verdict,
            factors={"conflicts_count": str(len(conflicts)), "holdings_count": str(len(holdings))},
            breakdown=breakdown
        )
        self.records.append(report)
        return report
