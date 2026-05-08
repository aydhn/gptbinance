from typing import Dict, List, Optional
from app.model_plane.models import EnsemblePolicy
from app.model_plane.exceptions import ModelPlaneError


class EnsembleGovernance:
    def __init__(self):
        self._policies: Dict[str, EnsemblePolicy] = {}

    def register_policy(self, policy: EnsemblePolicy) -> None:
        if not policy.policy_id:
            raise ModelPlaneError("Policy ID is required.")
        if not policy.model_refs:
            raise ModelPlaneError("Ensemble must contain model references.")

        self._policies[policy.policy_id] = policy

    def get_policy(self, policy_id: str) -> Optional[EnsemblePolicy]:
        return self._policies.get(policy_id)

    def validate_ensemble_consistency(self, policy_id: str) -> bool:
        policy = self.get_policy(policy_id)
        if not policy:
            return False

        if policy.weights and len(policy.weights) != len(policy.model_refs):
            return False

        return True
