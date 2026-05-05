from typing import List
from app.policy_kernel.models import PolicyGapFinding
from app.policy_kernel.enums import PolicyDomain, GapSeverity
import uuid

_GAP_REGISTRY: List[PolicyGapFinding] = []


def record_gap(
    domain: PolicyDomain, description: str, severity: GapSeverity, suggested_action: str
):
    record = PolicyGapFinding(
        gap_id=str(uuid.uuid4()),
        domain=domain,
        description=description,
        severity=severity,
        suggested_action=suggested_action,
    )
    _GAP_REGISTRY.append(record)
    return record


def list_gaps() -> List[PolicyGapFinding]:
    return _GAP_REGISTRY
