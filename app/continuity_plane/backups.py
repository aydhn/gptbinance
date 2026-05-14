from typing import Dict, List, Optional
from app.continuity_plane.models import BackupPolicy
from app.continuity_plane.exceptions import InvalidBackupPolicy

class BackupManager:
    def __init__(self):
        self._policies: Dict[str, BackupPolicy] = {}

    def register_policy(self, policy: BackupPolicy) -> None:
        if not policy.policy_id or not policy.service_id:
            raise InvalidBackupPolicy("policy_id and service_id must be provided")
        self._policies[policy.policy_id] = policy

    def get_policy(self, policy_id: str) -> Optional[BackupPolicy]:
        return self._policies.get(policy_id)

    def list_policies(self) -> List[BackupPolicy]:
        return list(self._policies.values())
