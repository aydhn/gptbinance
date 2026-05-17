import pytest
from app.environment_plane.storage import EnvironmentStorage
from app.environment_plane.objects import create_environment_object
from app.environment_plane.enums import EnvironmentClass

def test_environment_storage():
    storage = EnvironmentStorage()
    env = create_environment_object("env1", EnvironmentClass.STAGING, "owner", "desc")
    storage.save(env)

    fetched = storage.load("env1")
    assert fetched.environment_id == "env1"

    all_envs = storage.load_all()
    assert len(all_envs) == 1
