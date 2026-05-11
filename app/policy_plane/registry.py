from typing import Dict, List, Optional
from app.policy_plane.models import PolicyDefinition
from app.policy_plane.exceptions import InvalidPolicyDefinition


class CanonicalPolicyRegistry:
    def __init__(self):
        self._policies: Dict[str, PolicyDefinition] = {}

    def register(self, policy: PolicyDefinition) -> None:
        if not policy.policy_id:
            raise InvalidPolicyDefinition("Policy ID is required")
        self._policies[policy.policy_id] = policy

    def get_policy(self, policy_id: str) -> Optional[PolicyDefinition]:
        return self._policies.get(policy_id)

    def list_policies(self) -> List[PolicyDefinition]:
        return list(self._policies.values())

    def clear(self):
        self._policies.clear()


registry = CanonicalPolicyRegistry()
