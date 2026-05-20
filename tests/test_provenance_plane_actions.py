import pytest
from app.provenance_plane.actions import check_action_lineage
from app.provenance_plane.registry import registry

def test_check_action_lineage():
    registry.register("action-1", {"provenance_id": "action-1", "action_type": "system"})
    assert check_action_lineage("action-1") is True
