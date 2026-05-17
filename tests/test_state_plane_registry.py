import pytest
from app.state_plane.models import StateObject, LifecycleDefinition
from app.state_plane.registry import StateRegistry

def test_state_registry():
    registry = StateRegistry()

    lc = LifecycleDefinition(lifecycle_id="test_lc", states=["init", "ready", "terminal"], terminal_states=["terminal"])
    registry.register_lifecycle(lc)

    obj = StateObject(state_id="obj_1", object_class="test_class", lifecycle_id="test_lc")
    registry.register_object(obj)

    assert registry.get_object("obj_1") is not None
    assert registry.get_lifecycle("test_lc") is not None
