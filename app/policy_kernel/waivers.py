from typing import Dict, List, Optional
from datetime import datetime, timezone
from app.policy_kernel.models import PolicyWaiverDecision

_WAIVER_REGISTRY: Dict[str, PolicyWaiverDecision] = {}


def register_waiver(waiver: PolicyWaiverDecision):
    _WAIVER_REGISTRY[waiver.waiver_id] = waiver


def get_active_waiver(rule_id: str, scope: str) -> Optional[PolicyWaiverDecision]:
    now = datetime.now(timezone.utc)
    for waiver in _WAIVER_REGISTRY.values():
        if waiver.rule_id == rule_id and waiver.scope == scope and waiver.is_approved:
            if waiver.expires_at > now:
                return waiver
    return None


def list_active_waivers() -> List[PolicyWaiverDecision]:
    now = datetime.now(timezone.utc)
    return [
        w for w in _WAIVER_REGISTRY.values() if w.is_approved and w.expires_at > now
    ]
