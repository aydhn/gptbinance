import pytest
from app.state_plane.models import StateObject
from app.state_plane.registry import state_registry
from app.state_plane.desired import set_desired_state
from app.state_plane.effective import set_effective_state
from app.state_plane.reconciliation import reconcile_state

def test_reconciliation():
    obj = StateObject(state_id="obj_3", object_class="class_1", lifecycle_id="lc_1")
    state_registry.register_object(obj)

    set_desired_state("obj_3", "ready")
    set_effective_state("obj_3", "ready")

    rec = reconcile_state("obj_3")
    assert rec.is_converged is True

    set_effective_state("obj_3", "init")
    rec2 = reconcile_state("obj_3")
    assert rec2.is_converged is False
