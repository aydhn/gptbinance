from app.release_plane.models import ReleaseCandidateRef
from app.release_plane.exceptions import ReleasePlaneError
from typing import Optional
import uuid

class ReleaseControlRecord:
    def __init__(self, control_id: str, action: str, candidate_id: str, lineage_ref: str):
        self.control_id = control_id
        self.action = action
        self.candidate_ref = ReleaseCandidateRef(candidate_id=candidate_id)
        self.lineage_ref = lineage_ref
        self.proof_notes: Optional[str] = None

class ReleaseControlManager:
    def __init__(self):
        self._records = []

    def log_action(self, action: str, candidate_id: str, lineage_ref: str) -> ReleaseControlRecord:
        valid_actions = ["hold", "pause_rollout", "rollback_request", "hotfix_approval"]
        if action not in valid_actions:
             raise ReleasePlaneError(f"Invalid control action: {action}. No hidden manual release touches.")

        record = ReleaseControlRecord(
            control_id=f"ctl-{uuid.uuid4().hex[:8]}",
            action=action,
            candidate_id=candidate_id,
            lineage_ref=lineage_ref
        )
        self._records.append(record)
        return record
