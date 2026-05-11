import pytest
from app.policy_plane.registry import registry
from app.policy_plane.models import PolicyDefinition
from app.policy_plane.enums import PolicyClass


def test_registry_add_get():
    registry.clear()
    policy = PolicyDefinition(
        policy_id="POL-001",
        policy_class=PolicyClass.MANDATORY,
        description="Test Policy",
    )
    registry.register(policy)

    retrieved = registry.get_policy("POL-001")
    assert retrieved is not None
    assert retrieved.policy_id == "POL-001"

    assert len(registry.list_policies()) == 1
