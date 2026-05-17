import pytest
from app.state_plane.models import StateObject
from app.state_plane.registry import state_registry
from app.state_plane.observed import set_observed_state
from app.state_plane.declared import set_declared_state
from app.state_plane.split_brain import detect_split_brain

def test_split_brain():
    obj = StateObject(state_id="obj_4", object_class="class_1", lifecycle_id="lc_1")
    state_registry.register_object(obj)

    set_observed_state("obj_4", "running")
    set_declared_state("obj_4", "stopped")

    sb = detect_split_brain("obj_4")
    assert sb is not None
    assert sb.severity == "high"
