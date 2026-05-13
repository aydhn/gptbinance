import pytest
from app.continuity_plane.objectives import ContinuityObjectiveManager
from app.continuity_plane.models import ContinuityObjective, RtoTarget, RpoTarget
from app.continuity_plane.enums import ContinuityObjectiveClass

def test_objective_manager():
    manager = ContinuityObjectiveManager()
    obj = ContinuityObjective(
        objective_id="obj_1",
        service_id="srv_1",
        objective_class=ContinuityObjectiveClass.MAX_DATA_LOSS,
        rto=RtoTarget(target_seconds=3600),
        rpo=RpoTarget(target_seconds=600),
        description="Test Objective"
    )
    manager.register_objective(obj)

    retrieved = manager.get_objective("obj_1")
    assert retrieved is not None
    assert retrieved.objective_id == "obj_1"

    srv_objectives = manager.get_objectives_for_service("srv_1")
    assert len(srv_objectives) == 1
    assert srv_objectives[0].objective_id == "obj_1"
