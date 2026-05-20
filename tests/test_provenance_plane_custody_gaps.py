import pytest
from app.provenance_plane.custody_gaps import check_custody_gaps
from app.provenance_plane.registry import registry
from app.provenance_plane.exceptions import CustodyViolation

def test_custody_gap_detection():
    registry.register("gap-obj-1", {"provenance_id": "gap-obj-1", "custody_gap": True})
    with pytest.raises(CustodyViolation):
        check_custody_gaps("gap-obj-1")

def test_no_custody_gap():
    registry.register("no-gap-obj", {"provenance_id": "no-gap-obj", "custody_gap": False})
    severity = check_custody_gaps("no-gap-obj")
    assert severity == "LOW"
