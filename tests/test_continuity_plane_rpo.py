import pytest
from app.continuity_plane.rpo import RpoManager
from app.continuity_plane.models import RpoTarget

def test_rpo_manager():
    manager = RpoManager()
    target = RpoTarget(target_seconds=600, is_strict=True, caveats="none")
    manager.register_target("obj_1", target)

    retrieved = manager.get_target("obj_1")
    assert retrieved is not None
    assert retrieved.target_seconds == 600
