from datetime import datetime, timezone
from app.policy_plane.models import PolicyDefinition


def is_policy_active(policy: PolicyDefinition) -> bool:
    now = datetime.now(timezone.utc)
    if now < policy.effective_from:
        return False
    if policy.effective_until and now > policy.effective_until:
        return False
    return True
