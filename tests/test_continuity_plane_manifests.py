import pytest
from datetime import datetime, timezone
from app.continuity_plane.manifests import ContinuityManifestBuilder
from app.continuity_plane.models import ContinuityArtifactManifest

def test_manifest_builder():
    builder = ContinuityManifestBuilder()
    manifest = ContinuityArtifactManifest(
        manifest_id="man_1",
        service_id="srv_1",
        refs={"backup": "pol_1"},
        timestamp=datetime.now(timezone.utc)
    )
    builder.record_manifest(manifest)

    retrieved = builder.get_manifest("man_1")
    assert retrieved is not None
    assert retrieved.manifest_id == "man_1"
