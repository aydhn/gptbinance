from app.drift_plane.models import DriftTrustVerdict
from app.drift_plane.enums import TrustVerdict
from app.drift_plane.base import TrustEvaluatorBase

class TrustEvaluator(TrustEvaluatorBase):
    def evaluate_trust(self, drift_id: str) -> DriftTrustVerdict:
        return DriftTrustVerdict(
            verdict=TrustVerdict.TRUSTED
        )
