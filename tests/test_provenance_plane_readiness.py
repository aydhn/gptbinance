import pytest
from app.provenance_plane.readiness import get_provenance_readiness
from app.provenance_plane.registry import registry

def test_get_provenance_readiness():
    registry.register("obj-1", {"provenance_id": "obj-1", "is_ready": True})
    assert get_provenance_readiness("obj-1") is True
