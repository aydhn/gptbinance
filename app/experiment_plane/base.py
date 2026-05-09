from typing import List, Optional
from app.experiment_plane.models import (
    ExperimentDefinition,
    FairnessCheckResult,
    ExperimentTrustVerdict,
    ExperimentDecisionRecord,
)


class BaseExperimentRegistry:
    def register(self, experiment: ExperimentDefinition) -> None:
        raise NotImplementedError

    def get(self, experiment_id: str) -> Optional[ExperimentDefinition]:
        raise NotImplementedError

    def list_all(self) -> List[ExperimentDefinition]:
        raise NotImplementedError


class BaseFairnessEvaluator:
    def evaluate(self, experiment: ExperimentDefinition) -> FairnessCheckResult:
        raise NotImplementedError


class BaseStoppingEvaluator:
    def evaluate(self, experiment: ExperimentDefinition) -> ExperimentDecisionRecord:
        raise NotImplementedError


class BaseTrustEvaluator:
    def evaluate(
        self,
        experiment: ExperimentDefinition,
        fairness: FairnessCheckResult,
        decision: ExperimentDecisionRecord,
    ) -> ExperimentTrustVerdict:
        raise NotImplementedError
