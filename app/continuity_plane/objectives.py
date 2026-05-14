from typing import Dict, List, Optional
from app.continuity_plane.models import ContinuityObjective
from app.continuity_plane.exceptions import InvalidObjective

class ContinuityObjectiveManager:
    def __init__(self):
        self._objectives: Dict[str, ContinuityObjective] = {}

    def register_objective(self, objective: ContinuityObjective) -> None:
        if not objective.objective_id or not objective.service_id:
            raise InvalidObjective("objective_id and service_id must be provided")
        self._objectives[objective.objective_id] = objective

    def get_objective(self, objective_id: str) -> Optional[ContinuityObjective]:
        return self._objectives.get(objective_id)

    def list_objectives(self) -> List[ContinuityObjective]:
        return list(self._objectives.values())

    def get_objectives_for_service(self, service_id: str) -> List[ContinuityObjective]:
        return [obj for obj in self._objectives.values() if obj.service_id == service_id]
