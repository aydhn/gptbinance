from typing import Dict, List, Optional
from app.model_plane.models import ThresholdPolicy
from app.model_plane.exceptions import ThresholdPolicyViolation


class ThresholdPolicyRegistry:
    def __init__(self):
        self._policies: Dict[str, ThresholdPolicy] = {}

    def register_policy(self, policy: ThresholdPolicy) -> None:
        if not policy.policy_id:
            raise ThresholdPolicyViolation("Policy ID is required.")
        if not policy.model_id:
            raise ThresholdPolicyViolation("Model ID is required.")

        self._policies[policy.policy_id] = policy

    def get_policy(self, policy_id: str) -> Optional[ThresholdPolicy]:
        return self._policies.get(policy_id)

    def get_policies_for_model(self, model_id: str) -> List[ThresholdPolicy]:
        return [p for p in self._policies.values() if p.model_id == model_id]

    def validate_threshold_usage(
        self, model_id: str, provided_policy_id: Optional[str]
    ) -> bool:
        if provided_policy_id:
            policy = self.get_policy(provided_policy_id)
            if not policy or policy.model_id != model_id:
                return False
        return True
