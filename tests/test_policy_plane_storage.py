import pytest
from app.policy_plane.repository import PolicyRepository
from app.policy_plane.models import PolicyDefinition
from app.policy_plane.enums import PolicyClass


def test_policy_storage():
    repo = PolicyRepository()
    policy = PolicyDefinition(
        policy_id="POL-STORAGE-1",
        policy_class=PolicyClass.MANDATORY,
        description="Storage test",
    )
    repo.save_policy(policy)

    loaded = repo.get_policy("POL-STORAGE-1")
    assert loaded is not None
    assert loaded.policy_id == "POL-STORAGE-1"
