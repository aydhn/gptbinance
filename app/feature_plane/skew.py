from app.feature_plane.models import FeatureSkewReport
from app.feature_plane.enums import SkewSeverity


class SkewEvaluator:
    def evaluate_skew(self, feature_id: str) -> FeatureSkewReport:
        return FeatureSkewReport(
            report_id=f"skew_{feature_id}",
            severity=SkewSeverity.NONE,
            suspected_causes=[],
            impact_hints=[],
        )
