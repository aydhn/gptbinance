import pytest
from app.autonomy_plane.execution import check_execution_provenance

def test_autonomous_action_blocked():
    assert "CAUTION" in check_execution_provenance("auto-1", [])
    assert "TRUSTED" in check_execution_provenance("auto-2", ["ref1"])
