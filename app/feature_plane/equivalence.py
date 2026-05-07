from app.feature_plane.models import FeatureEquivalenceReport
from app.feature_plane.enums import EquivalenceVerdict


class EquivalenceEvaluator:
    def evaluate(
        self, context_a: str, context_b: str, manifest_id: str
    ) -> FeatureEquivalenceReport:
        return FeatureEquivalenceReport(
            report_id=f"equiv_{context_a}_{context_b}",
            context_a=context_a,
            context_b=context_b,
            verdict=EquivalenceVerdict.EQUIVALENT,
            differences={},
        )
