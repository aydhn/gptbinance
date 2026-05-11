import pytest
from app.policy_plane.temporal import is_policy_active
from app.policy_plane.models import PolicyDefinition
from app.policy_plane.enums import PolicyClass
from datetime import datetime, timedelta, timezone


def test_policy_active():
    now = datetime.now(timezone.utc)
    policy = PolicyDefinition(
        policy_id="POL-TEMP",
        policy_class=PolicyClass.MANDATORY,
        description="Temp",
        effective_from=now - timedelta(days=1),
        effective_until=now + timedelta(days=1),
    )
    assert is_policy_active(policy)


def test_policy_inactive():
    now = datetime.now(timezone.utc)
    policy = PolicyDefinition(
        policy_id="POL-TEMP",
        policy_class=PolicyClass.MANDATORY,
        description="Temp",
        effective_from=now - timedelta(days=2),
        effective_until=now - timedelta(days=1),
    )
    assert not is_policy_active(policy)
