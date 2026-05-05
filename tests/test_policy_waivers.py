import pytest
from datetime import datetime, timezone, timedelta
from app.policy_kernel.models import PolicyWaiverDecision
from app.policy_kernel.waivers import register_waiver, get_active_waiver


def test_waivers():
    now = datetime.now(timezone.utc)
    waiver = PolicyWaiverDecision(
        waiver_id="W1",
        rule_id="R1",
        approver="test",
        is_approved=True,
        expires_at=now + timedelta(hours=1),
        scope="testnet",
    )
    register_waiver(waiver)

    assert get_active_waiver("R1", "testnet") == waiver
    assert get_active_waiver("R1", "live") is None
