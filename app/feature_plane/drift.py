from app.feature_plane.models import FeatureDriftReport
from app.feature_plane.enums import DriftSeverity


class DriftEvaluator:
    def evaluate_drift(self, manifest_id: str) -> FeatureDriftReport:
        return FeatureDriftReport(
            report_id=f"drift_{manifest_id}",
            severity=DriftSeverity.NONE,
            drifted_features=[],
            explanations=[],
        )
