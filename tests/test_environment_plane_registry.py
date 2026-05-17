import pytest
from app.environment_plane.registry import CanonicalEnvironmentRegistry
from app.environment_plane.objects import create_environment_object
from app.environment_plane.enums import EnvironmentClass
from app.environment_plane.exceptions import InvalidEnvironmentObjectError

def test_registry_register_and_get():
    registry = CanonicalEnvironmentRegistry()
    env = create_environment_object("test-env-1", EnvironmentClass.LOCAL_DEV, "owner-1", "description")

    registry.register(env)

    fetched = registry.get("test-env-1")
    assert fetched.environment_id == "test-env-1"
    assert fetched.record.owner == "owner-1"

def test_registry_get_not_found():
    registry = CanonicalEnvironmentRegistry()
    with pytest.raises(InvalidEnvironmentObjectError):
        registry.get("non-existent")

def test_registry_list_all():
    registry = CanonicalEnvironmentRegistry()
    env1 = create_environment_object("env-1", EnvironmentClass.LOCAL_DEV, "owner", "desc")
    env2 = create_environment_object("env-2", EnvironmentClass.STAGING, "owner", "desc")

    registry.register(env1)
    registry.register(env2)

    all_envs = registry.list_all()
    assert len(all_envs) == 2
