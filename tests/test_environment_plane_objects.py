import pytest
from app.environment_plane.objects import create_environment_object
from app.environment_plane.enums import EnvironmentClass
from app.environment_plane.models import EnvironmentObject

def test_create_environment_object():
    env = create_environment_object("test-env-1", EnvironmentClass.REPLAY, "owner-1", "desc")
    assert isinstance(env, EnvironmentObject)
    assert env.environment_id == "test-env-1"
    assert env.record.environment_class == EnvironmentClass.REPLAY
    assert env.record.owner == "owner-1"
    assert env.record.description == "desc"
    assert env.record.created_at is not None
