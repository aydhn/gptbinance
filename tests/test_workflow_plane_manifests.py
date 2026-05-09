from app.workflow_plane.manifests import ManifestBuilder

def test_manifest_building():
    builder = ManifestBuilder()
    m = builder.build_manifest("wf-1", "r-1", ["art-1", "art-2"])
    assert "art-1" in m.artifacts
