from app.feature_plane.models import TrustedFeatureVerdictSummary
from app.feature_plane.enums import (
    TrustedFeatureVerdict,
    LeakageSeverity,
    SkewSeverity,
    DriftSeverity,
)


class TrustedFeatureVerdictEngine:
    def evaluate(self, manifest_id: str) -> TrustedFeatureVerdictSummary:
        return TrustedFeatureVerdictSummary(
            verdict=TrustedFeatureVerdict.TRUSTED,
            point_in_time_valid=True,
            leakage_severity=LeakageSeverity.NONE,
            skew_severity=SkewSeverity.NONE,
            drift_severity=DriftSeverity.NONE,
            has_freshness_issues=False,
            blocker_reasons=[],
        )
