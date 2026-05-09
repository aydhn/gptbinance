from app.experiment_plane.models import ExperimentDefinition, FairnessCheckResult
from app.experiment_plane.base import BaseFairnessEvaluator
from app.experiment_plane.enums import FairnessClass


class StandardFairnessEvaluator(BaseFairnessEvaluator):
    def evaluate(self, experiment: ExperimentDefinition) -> FairnessCheckResult:
        # Dummy logic for demonstration
        is_fair = True
        imbalances = {}

        # Example check: exposure split shouldn't be too small for candidate
        # Real implementation would check real execution data
        if not is_fair:
            return FairnessCheckResult(
                fairness_class=FairnessClass.IMBALANCED_EXPOSURE,
                severity="HIGH",
                rationale="Significant exposure imbalance detected.",
                imbalances=imbalances,
            )

        return FairnessCheckResult(
            fairness_class=FairnessClass.FAIR,
            severity="NONE",
            rationale="No significant fairness violations detected.",
        )
