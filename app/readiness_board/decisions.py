from typing import Dict, Any, List

class FinalBoardDecision:
    def __init__(self, decision_id: str, candidate_id: str, decision: str, activation_class: str, scope: Dict[str, Any]):
        self.decision_id = decision_id
        self.candidate_id = candidate_id
        self.decision = decision
        self.activation_class = activation_class
        self.scope = scope

    def export_for_activation(self) -> Dict[str, Any]:
        return {
            "decision_id": self.decision_id,
            "candidate_id": self.candidate_id,
            "decision": self.decision,
            "activation_class": self.activation_class,
            "scope": self.scope,
            "forbidden_expansions": ["full_live_auto"],
            "probation_requirements": {"duration_minutes": 60}
        }
