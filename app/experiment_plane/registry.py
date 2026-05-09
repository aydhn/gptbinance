from typing import Dict, List, Optional
from app.experiment_plane.models import ExperimentDefinition
from app.experiment_plane.base import BaseExperimentRegistry
from app.experiment_plane.exceptions import InvalidExperimentDefinitionError


class CanonicalExperimentRegistry(BaseExperimentRegistry):
    def __init__(self) -> None:
        self._registry: Dict[str, ExperimentDefinition] = {}

    def register(self, experiment: ExperimentDefinition) -> None:
        if not experiment.experiment_id:
            raise InvalidExperimentDefinitionError("Experiment must have an ID")
        if experiment.experiment_id in self._registry:
            raise InvalidExperimentDefinitionError(
                f"Experiment {experiment.experiment_id} already registered"
            )
        if not experiment.arms:
            raise InvalidExperimentDefinitionError(
                "Experiment must have at least one arm"
            )
        if not experiment.objective:
            raise InvalidExperimentDefinitionError("Experiment must have an objective")

        # Verify no undocumented arms
        for arm in experiment.arms:
            if not arm.description:
                raise InvalidExperimentDefinitionError(
                    f"Arm {arm.arm_id} missing description"
                )

        self._registry[experiment.experiment_id] = experiment

    def get(self, experiment_id: str) -> Optional[ExperimentDefinition]:
        return self._registry.get(experiment_id)

    def list_all(self) -> List[ExperimentDefinition]:
        return list(self._registry.values())
