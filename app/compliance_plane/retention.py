from app.compliance_plane.models import RetentionPolicy
from typing import Dict, List


class RetentionManager:
    def __init__(self):
        self._policies: Dict[str, RetentionPolicy] = {}

    def register_policy(self, policy: RetentionPolicy) -> None:
        self._policies[policy.retention_id] = policy

    def get_policy(self, retention_id: str) -> RetentionPolicy:
        return self._policies.get(retention_id)

    def list_policies(self) -> List[RetentionPolicy]:
        return list(self._policies.values())
