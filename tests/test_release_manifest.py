import pytest
from app.release.manifest import ManifestGenerator


def test_create_manifest():
    gen = ManifestGenerator()
    manifest = gen.create_manifest()
    assert manifest.version.version == "1.0.0"
    assert "core" in [c.name for c in manifest.components]
