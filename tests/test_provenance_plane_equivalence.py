import pytest
from app.provenance_plane.equivalence import get_equivalence
from app.provenance_plane.registry import registry

def test_get_equivalence():
    registry.register("obj-1", {"provenance_id": "obj-1", "equivalence_verdict": "EQUIVALENT"})
    assert get_equivalence("obj-1") == "EQUIVALENT"
