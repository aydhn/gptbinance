import pytest
from app.environment_plane.manifests import build_manifest

def test_build_manifest():
    manifest = build_manifest("hash123", "ref123")
    assert manifest.artifact_hash == "hash123"
    assert manifest.lineage_refs == "ref123"
