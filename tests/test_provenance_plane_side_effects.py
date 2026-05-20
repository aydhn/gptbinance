import pytest
from app.provenance_plane.side_effects import check_side_effects
from app.provenance_plane.registry import registry

def test_check_side_effects():
    registry.register("action-2", {"provenance_id": "action-2", "side_effects": ["database_update"]})
    assert check_side_effects("action-2") is True
