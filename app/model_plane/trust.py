from typing import Dict, Any, List
from datetime import datetime, timezone
from app.model_plane.models import TrustedSignalVerdictSummary, InferenceManifestEntry
from app.model_plane.enums import TrustedSignalVerdict
from app.model_plane.freshness import ModelFreshnessEvaluator
from app.model_plane.uncertainty import UncertaintyManager


class TrustedSignalVerdictEngine:
    def __init__(
        self,
        freshness_evaluator: ModelFreshnessEvaluator,
        uncertainty_manager: UncertaintyManager,
    ):
        self.freshness_evaluator = freshness_evaluator
        self.uncertainty_manager = uncertainty_manager

    def evaluate(
        self, entry: InferenceManifestEntry, feature_trust_degraded: bool = False
    ) -> TrustedSignalVerdictSummary:
        blockers = []
        factors = {}
        verdict = TrustedSignalVerdict.TRUSTED

        freshness_results = self.freshness_evaluator.evaluate_all(entry.checkpoint_id)
        factors["freshness"] = freshness_results

        if freshness_results.get("checkpoint_stale"):
            blockers.append("Checkpoint is stale")
            verdict = TrustedSignalVerdict.CAUTION

        if freshness_results.get("calibration_stale"):
            blockers.append("Calibration is stale")
            verdict = TrustedSignalVerdict.DEGRADED

        if feature_trust_degraded:
            blockers.append("Feature input trust is degraded")
            verdict = TrustedSignalVerdict.DEGRADED

        if not self.uncertainty_manager.check_low_confidence_gate(entry.checkpoint_id):
            blockers.append("Failed low confidence gate")
            verdict = TrustedSignalVerdict.BLOCKED

        return TrustedSignalVerdictSummary(
            model_id=entry.model_ref.model_id,
            verdict=verdict,
            evaluated_at=datetime.now(timezone.utc),
            factors=factors,
            blocker_reasons=blockers,
        )
