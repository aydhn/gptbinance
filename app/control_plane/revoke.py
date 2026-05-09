from typing import Dict
from app.control_plane.models import ActionRevokeRecord


class RevokeEngine:
    def __init__(self):
        self._revocations: Dict[str, ActionRevokeRecord] = {}

    def revoke_target(
        self, target_id: str, actor: str, reason: str
    ) -> ActionRevokeRecord:
        record = ActionRevokeRecord(target_id=target_id, actor=actor, reason=reason)
        self._revocations[target_id] = record
        return record
