import pytest
from app.provenance_plane.approvals import check_approval_lineage
from app.provenance_plane.registry import registry

def test_check_approval_lineage():
    registry.register("approval-1", {"provenance_id": "approval-1", "approved_by": "user1"})
    assert check_approval_lineage("approval-1") is True
