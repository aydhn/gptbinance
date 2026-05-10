import pytest
from app.release_plane.environments import env_registry
from app.release_plane.enums import EnvironmentClass
from app.release_plane.exceptions import ReleasePlaneError
from app.release_plane.models import EnvironmentTarget

def test_core_environments_exist():
    replay_env = env_registry.get(EnvironmentClass.REPLAY)
    assert replay_env is not None
    assert replay_env.environment_class == EnvironmentClass.REPLAY

    live_full = env_registry.get(EnvironmentClass.LIVE_FULL)
    assert live_full is not None

def test_reject_hidden_aliases():
    target = EnvironmentTarget(environment_class=EnvironmentClass.REPLAY, isolation_rules={}, metadata={})
    with pytest.raises(ReleasePlaneError):
         env_registry.register(target)
