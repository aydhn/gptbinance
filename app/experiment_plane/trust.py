from app.experiment_plane.models import (
    ExperimentDefinition,
    FairnessCheckResult,
    ExperimentDecisionRecord,
    ExperimentTrustVerdict,
)
from app.experiment_plane.base import BaseTrustEvaluator
from app.experiment_plane.enums import TrustVerdict, FairnessClass, StoppingClass


class StandardTrustEvaluator(BaseTrustEvaluator):
    def evaluate(
        self,
        experiment: ExperimentDefinition,
        fairness: FairnessCheckResult,
        decision: ExperimentDecisionRecord,
    ) -> ExperimentTrustVerdict:
        if fairness.fairness_class != FairnessClass.FAIR:
            return ExperimentTrustVerdict(
                verdict=TrustVerdict.CAUTION,
                breakdown={"fairness": str(fairness.fairness_class.value)},
                proof_notes="Fairness issues detected.",
            )

        if decision.stopping_class in [
            StoppingClass.STOP_FOR_HARM,
            StoppingClass.STOP_FOR_DRIFT,
            StoppingClass.STOP_FOR_INCOMPARABILITY,
        ]:
            return ExperimentTrustVerdict(
                verdict=TrustVerdict.BLOCKED,
                breakdown={"stopping": str(decision.stopping_class.value)},
                proof_notes="Stopping rule triggered.",
            )

        return ExperimentTrustVerdict(
            verdict=TrustVerdict.TRUSTED,
            breakdown={"all": "passed"},
            proof_notes="Experiment passed all integrity checks.",
        )
