import pytest
from app.state_plane.models import StateObject
from app.state_plane.registry import state_registry
from app.state_plane.observed import set_observed_state
from app.state_plane.declared import set_declared_state
from app.state_plane.split_brain import detect_split_brain
from app.state_plane.trust import evaluate_trust
from app.state_plane.enums import TrustVerdict

def test_evaluate_trust():
    obj = StateObject(state_id="obj_5", object_class="class_1", lifecycle_id="lc_1")
    state_registry.register_object(obj)

    set_observed_state("obj_5", "running")
    set_declared_state("obj_5", "stopped")
    detect_split_brain("obj_5")

    trust = evaluate_trust("obj_5")
    assert trust.verdict == TrustVerdict.BLOCKED.value
