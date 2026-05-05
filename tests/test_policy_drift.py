import pytest
from app.policy_kernel.drift import record_drift, list_drifts
from app.policy_kernel.enums import PolicyVerdict, DriftSeverity


def test_record_drift():
    record = record_drift(
        "module_x", PolicyVerdict.HARD_BLOCK, PolicyVerdict.ALLOW, "test", "Fix it"
    )
    assert record.severity == DriftSeverity.CRITICAL
    assert record in list_drifts()
