from typing import Dict, List, Optional

from .models import ReliabilityObjective


class ReliabilityObjectiveManager:
    def __init__(self, registry):
        self._registry = registry

    def register_objective(self, objective: ReliabilityObjective) -> None:
        self._registry.register_objective(objective)

    def get_objective(self, objective_id: str) -> Optional[ReliabilityObjective]:
        return self._registry.get_objective(objective_id)

    def list_objectives(self) -> List[ReliabilityObjective]:
        return self._registry.list_objectives()
