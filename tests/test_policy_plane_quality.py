import pytest
from app.policy_plane.quality import assess_policy_quality
from app.policy_plane.models import PolicyDefinition
from app.policy_plane.enums import PolicyClass


def test_assess_policy_quality():
    policy = PolicyDefinition(
        policy_id="POL-Q-1",
        policy_class=PolicyClass.MANDATORY,
        description="Empty policy",
    )
    res = assess_policy_quality(policy)
    assert res["quality"] == "poor"
    assert "No rules defined" in res["warnings"]
