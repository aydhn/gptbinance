import pytest
from app.state_plane.models import StateObject, LifecycleDefinition
from app.state_plane.registry import state_registry
from app.state_plane.transitions import record_transition
from app.state_plane.exceptions import IllegalStateJumpError

def test_transition():
    lc = LifecycleDefinition(lifecycle_id="lc_1", states=["a", "b", "c"], terminal_states=["c"])
    state_registry.register_lifecycle(lc)

    obj = StateObject(state_id="obj_2", object_class="class_1", lifecycle_id="lc_1")
    state_registry.register_object(obj)

    t = record_transition("obj_2", "a", "b")
    assert t.to_state == "b"

    with pytest.raises(IllegalStateJumpError):
        record_transition("obj_2", "b", "d")
