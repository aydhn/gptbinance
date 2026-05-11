from app.policy_plane.models import PolicyExceptionRecord
from app.policy_plane.enums import ExceptionClass
from datetime import datetime, timedelta, timezone


def issue_scoped_exception(
    policy_id: str, issuer_id: str, reason: str, ttl_minutes: int, scope: dict
) -> PolicyExceptionRecord:
    now = datetime.now(timezone.utc)
    return PolicyExceptionRecord(
        exception_class=ExceptionClass.SCOPED,
        policy_id=policy_id,
        scope_constraints=scope,
        ttl_minutes=ttl_minutes,
        reason=reason,
        issuer_id=issuer_id,
        expires_at=now + timedelta(minutes=ttl_minutes),
    )
