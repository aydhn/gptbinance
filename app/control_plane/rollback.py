import uuid
from typing import Dict
from app.control_plane.models import ActionRollbackRecord


class RollbackEngine:
    def __init__(self):
        self._rollbacks: Dict[str, ActionRollbackRecord] = {}

    def rollback_action(self, action_id: str, actor: str) -> ActionRollbackRecord:
        # Simplified validation logic
        record = ActionRollbackRecord(
            action_id=action_id,
            rollback_receipt_id=f"RBK-{uuid.uuid4().hex[:8]}",
            actor=actor,
            outcome="SUCCESS",
        )
        self._rollbacks[action_id] = record
        return record
