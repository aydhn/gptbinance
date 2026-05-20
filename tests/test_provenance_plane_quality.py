import pytest
from app.provenance_plane.quality import get_quality
from app.provenance_plane.registry import registry

def test_get_quality():
    registry.register("obj-1", {"provenance_id": "obj-1", "quality_verdict": "HIGH"})
    assert get_quality("obj-1") == "HIGH"
