import pytest
from app.policy_kernel.gaps import record_gap, list_gaps
from app.policy_kernel.enums import PolicyDomain, GapSeverity


def test_record_gap():
    record = record_gap(
        PolicyDomain.RISK, "Missing invariant", GapSeverity.HIGH, "Add it"
    )
    assert record in list_gaps()
