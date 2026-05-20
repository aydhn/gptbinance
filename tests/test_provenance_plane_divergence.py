import pytest
from app.provenance_plane.divergence import get_divergence
from app.provenance_plane.registry import registry

def test_get_divergence():
    registry.register("obj-1", {"provenance_id": "obj-1", "divergence_severity": "LOW"})
    assert get_divergence("obj-1") == "LOW"
