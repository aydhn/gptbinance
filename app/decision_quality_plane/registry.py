from typing import Dict, List
from app.decision_quality_plane.models import DecisionDefinition
from app.decision_quality_plane.exceptions import InvalidDecisionDefinitionError

class CanonicalDecisionRegistry:
    def __init__(self):
        self._decisions: Dict[str, DecisionDefinition] = {}

    def register(self, decision: DecisionDefinition) -> None:
        if not decision.decision_id or not decision.decision_class:
            raise InvalidDecisionDefinitionError("Missing critical decision fields")
        self._decisions[decision.decision_id] = decision

    def get(self, decision_id: str) -> DecisionDefinition:
        return self._decisions.get(decision_id)

    def list_all(self) -> List[DecisionDefinition]:
        return list(self._decisions.values())
