import uuid
from typing import List
from app.performance_plane.enums import TrustVerdict
from app.performance_plane.models import PerformanceTrustVerdict


class FeatureTrustEvaluator:
    @staticmethod
    def evaluate(
        feature_id: str, freshness_seconds: int, completeness_ratio: float
    ) -> dict:
        score = 100
        if freshness_seconds > 300:
            score -= 40
        if completeness_ratio < 0.95:
            score -= 20

        verdict = "healthy"
        if score < 60:
            verdict = "degraded"

        return {"feature_id": feature_id, "score": score, "verdict": verdict}

    @staticmethod
    def export_attribution_quality_caveat(
        feature_id: str, verdict: str
    ) -> PerformanceTrustVerdict:
        trust_verdict = TrustVerdict.TRUSTED
        blockers = []
        if verdict == "degraded":
            trust_verdict = TrustVerdict.CAUTION
            blockers.append(
                f"Feature {feature_id} integrity degraded, upstream performance attribution quality is uncertain."
            )

        return PerformanceTrustVerdict(
            verdict_id=str(uuid.uuid4()),
            manifest_id="dummy",  # Replaced dynamically
            verdict=trust_verdict,
            blockers=blockers,
            factors={"feature_verdict": verdict},
        )
