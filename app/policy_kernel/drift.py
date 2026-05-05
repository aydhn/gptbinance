from typing import List
from app.policy_kernel.models import PolicyDriftRecord
from app.policy_kernel.enums import PolicyVerdict, DriftSeverity
import uuid

_DRIFT_REGISTRY: List[PolicyDriftRecord] = []


def record_drift(
    module_name: str,
    declared_verdict: PolicyVerdict,
    actual_verdict: PolicyVerdict,
    action_type: str,
    remediation_suggestion: str,
):
    # Determine severity
    severity = DriftSeverity.LOW
    if (
        declared_verdict == PolicyVerdict.HARD_BLOCK
        and actual_verdict != PolicyVerdict.HARD_BLOCK
    ):
        severity = DriftSeverity.CRITICAL
    elif (
        declared_verdict == PolicyVerdict.BLOCK
        and actual_verdict == PolicyVerdict.ALLOW
    ):
        severity = DriftSeverity.HIGH

    record = PolicyDriftRecord(
        drift_id=str(uuid.uuid4()),
        module_name=module_name,
        declared_verdict=declared_verdict,
        actual_verdict=actual_verdict,
        action_type=action_type,
        severity=severity,
        remediation_suggestion=remediation_suggestion,
    )
    _DRIFT_REGISTRY.append(record)
    return record


def list_drifts() -> List[PolicyDriftRecord]:
    return _DRIFT_REGISTRY
