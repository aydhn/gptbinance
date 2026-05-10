from datetime import timezone
from datetime import datetime, timedelta
from typing import Optional
from app.release_plane.exceptions import RolloutViolation

class HoldRecord:
    def __init__(self, hold_id: str, candidate_id: str, hold_type: str, ttl_seconds: int, reason: str):
        self.hold_id = hold_id
        self.candidate_id = candidate_id
        self.hold_type = hold_type  # approval_hold, readiness_hold, risk_hold, incident_hold, operator_hold
        self.reason = reason
        self.expires_at = datetime.now(timezone.utc) + timedelta(seconds=ttl_seconds)
        self.proof_notes: Optional[str] = None

class HoldManager:
    def __init__(self):
        self._holds = {}

    def apply_hold(self, candidate_id: str, hold_type: str, ttl_seconds: int, reason: str) -> HoldRecord:
        import uuid
        hold = HoldRecord(
            hold_id=f"hold-{uuid.uuid4().hex[:8]}",
            candidate_id=candidate_id,
            hold_type=hold_type,
            ttl_seconds=ttl_seconds,
            reason=reason
        )
        self._holds[hold.hold_id] = hold
        return hold

    def release_hold(self, hold_id: str, approver: str, proof_notes: str) -> None:
        if hold_id not in self._holds:
             raise RolloutViolation("Hold not found.")

        hold = self._holds[hold_id]
        if datetime.now(timezone.utc) > hold.expires_at:
             raise RolloutViolation("Hold TTL expired, review requirements not met.")

        hold.proof_notes = proof_notes
        # Hold removal logic would complete here
        del self._holds[hold_id]
