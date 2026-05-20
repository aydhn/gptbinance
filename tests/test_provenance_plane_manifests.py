import pytest
from app.provenance_plane.manifests import generate_manifest
from app.provenance_plane.registry import registry

def test_generate_manifest():
    registry.register("obj-1", {"provenance_id": "obj-1", "test": "data"})
    manifest = generate_manifest("obj-1")
    assert manifest["manifest_id"] == "man_obj-1"
