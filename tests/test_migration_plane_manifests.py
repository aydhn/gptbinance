import pytest
from app.migration_plane.manifests import ManifestBuilder

def test_build_manifest():
    builder = ManifestBuilder()
    result = builder.build_manifest("mig_001", "hash123", ["ref1"], {"key": "val"})
    assert result.hash_value == "hash123"
    assert len(result.lineage_refs) == 1
