from app.cost_plane.manifests import ManifestBuilder

def test_manifest_builder():
    builder = ManifestBuilder()
    manifest = builder.build_manifest(["c-1"], [], [], [])
    assert manifest.cost_refs == ["c-1"]
