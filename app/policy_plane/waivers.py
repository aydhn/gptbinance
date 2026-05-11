from app.policy_plane.models import PolicyWaiverRecord
from datetime import datetime, timedelta, timezone


def request_waiver(
    policy_id: str, requester_id: str, reason: str, scope: dict, ttl_minutes: int
) -> PolicyWaiverRecord:
    now = datetime.now(timezone.utc)
    return PolicyWaiverRecord(
        policy_id=policy_id,
        requester_id=requester_id,
        reason=reason,
        scope_constraints=scope,
        expires_at=now + timedelta(minutes=ttl_minutes),
    )


def approve_waiver(waiver: PolicyWaiverRecord, approver_id: str):
    waiver.approver_id = approver_id
