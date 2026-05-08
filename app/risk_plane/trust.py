from app.risk_plane.models import RiskState
from app.performance_plane.enums import TrustVerdict
from app.performance_plane.models import PerformanceTrustVerdict
import uuid


class RiskTrustEvaluator:
    @staticmethod
    def evaluate(state: RiskState) -> float:
        # Dummy evaluation logic
        return 1.0

    @staticmethod
    def export_trust_verdict(state: RiskState) -> PerformanceTrustVerdict:
        verdict = TrustVerdict.TRUSTED
        blockers = []
        if not state.authoritative:
            verdict = TrustVerdict.DEGRADED
            blockers.append("Risk state is non-authoritative.")

        return PerformanceTrustVerdict(
            verdict_id=str(uuid.uuid4()),
            manifest_id="dummy",  # Replaced dynamically
            verdict=verdict,
            blockers=blockers,
            factors={"authoritative": state.authoritative},
        )
