import pytest
from app.observability_plane.storage import ObservabilityStorageEngine
from app.observability_plane.repository import ObservabilityRepository
from app.observability_plane.models import ObservabilityArtifactManifest, ObservabilityTrustVerdict
from app.observability_plane.enums import TrustVerdict

def test_storage_and_repository():
    storage = ObservabilityStorageEngine()
    repo = ObservabilityRepository(storage)

    trust = ObservabilityTrustVerdict(verdict=TrustVerdict.TRUSTED, factors={})
    manifest = ObservabilityArtifactManifest(manifest_id="m1", telemetry_refs=[], trust_verdict=trust)

    repo.save_manifest(manifest)
    assert repo.get_manifest("m1").manifest_id == "m1"
