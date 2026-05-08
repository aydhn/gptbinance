import uuid
from typing import List
from app.performance_plane.enums import TrustVerdict
from app.performance_plane.models import PerformanceTrustVerdict


class ModelTrustEvaluator:
    @staticmethod
    def evaluate(model_id: str, drift_score: float, calibration_error: float) -> dict:
        score = 100
        if drift_score > 0.2:
            score -= 30
        if calibration_error > 0.1:
            score -= 20

        verdict = "healthy"
        if score < 70:
            verdict = "degraded"

        return {"model_id": model_id, "score": score, "verdict": verdict}

    @staticmethod
    def export_trust_caveat(model_id: str, verdict: str) -> PerformanceTrustVerdict:
        trust_verdict = TrustVerdict.TRUSTED
        blockers = []
        if verdict == "degraded":
            trust_verdict = TrustVerdict.CAUTION
            blockers.append(
                f"Model {model_id} has degraded trust, signal selection attribution may be flawed."
            )

        return PerformanceTrustVerdict(
            verdict_id=str(uuid.uuid4()),
            manifest_id="dummy",  # Replaced dynamically
            verdict=trust_verdict,
            blockers=blockers,
            factors={"model_verdict": verdict},
        )
