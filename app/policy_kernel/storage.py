from typing import Dict, List
from app.policy_kernel.models import PolicyDecision
from app.policy_kernel.conflicts import PolicyConflict

_DECISION_REGISTRY: Dict[str, PolicyDecision] = {}
_CONFLICT_REGISTRY: Dict[str, List[PolicyConflict]] = {}


def store_decision(decision: PolicyDecision):
    _DECISION_REGISTRY[decision.decision_id] = decision


def get_decision(decision_id: str) -> PolicyDecision:
    return _DECISION_REGISTRY.get(decision_id)


def store_conflicts(action_id: str, conflicts: List[PolicyConflict]):
    _CONFLICT_REGISTRY[action_id] = conflicts


def get_conflicts(action_id: str) -> List[PolicyConflict]:
    return _CONFLICT_REGISTRY.get(action_id, [])
