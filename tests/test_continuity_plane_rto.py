import pytest
from app.continuity_plane.rto import RtoManager
from app.continuity_plane.models import RtoTarget

def test_rto_manager():
    manager = RtoManager()
    target = RtoTarget(target_seconds=3600, is_strict=True, caveats="none")
    manager.register_target("obj_1", target)

    retrieved = manager.get_target("obj_1")
    assert retrieved is not None
    assert retrieved.target_seconds == 3600
