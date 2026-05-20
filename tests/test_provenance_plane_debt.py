import pytest
from app.provenance_plane.debt import get_provenance_debt
from app.provenance_plane.registry import registry

def test_get_provenance_debt():
    registry.register("obj-1", {"provenance_id": "obj-1", "debt_score": 5})
    assert get_provenance_debt("obj-1") == 5
