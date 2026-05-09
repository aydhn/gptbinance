from app.experiment_plane.models import (
    ExperimentDefinition,
    ExperimentDecisionRecord,
)
from app.experiment_plane.base import BaseStoppingEvaluator
from app.experiment_plane.enums import StoppingClass


class StandardStoppingEvaluator(BaseStoppingEvaluator):
    def evaluate(self, experiment: ExperimentDefinition) -> ExperimentDecisionRecord:
        # Dummy logic: check rules
        for rule in experiment.stopping_rules:
            if "harm" in rule.condition.lower():
                # simulate check
                pass

        return ExperimentDecisionRecord(
            decision_id=f"dec_{experiment.experiment_id}",
            stopping_class=StoppingClass.CONTINUE,
            rationale="No stopping rules triggered.",
            evidence_refs=[],
        )
