from typing import Dict, List, Optional
from app.value_plane.models import ValueObjective
from app.value_plane.exceptions import InvalidObjectiveDefinition

class ObjectiveRegistry:
    def __init__(self):
        self._objectives: Dict[str, ValueObjective] = {}

    def register(self, objective: ValueObjective):
        if not objective.measurable_success_criteria:
            raise InvalidObjectiveDefinition("Objective must have measurable success criteria")
        self._objectives[objective.objective_id] = objective

    def get(self, objective_id: str) -> Optional[ValueObjective]:
        return self._objectives.get(objective_id)

    def list_all(self) -> List[ValueObjective]:
        return list(self._objectives.values())

objective_registry = ObjectiveRegistry()
