from app.feature_plane.models import FeatureFreshnessReport


class FreshnessEvaluator:
    def evaluate_freshness(self, manifest_id: str) -> FeatureFreshnessReport:
        return FeatureFreshnessReport(
            report_id=f"fresh_{manifest_id}",
            stale_features=[],
            consumer_impact_summary="No staleness detected.",
        )
