import pytest
from app.observability_plane.manifests import ManifestBuilder
from app.observability_plane.models import ObservabilityArtifactManifest, ObservabilityTrustVerdict
from app.observability_plane.enums import TrustVerdict

def test_manifest_building():
    builder = ManifestBuilder()
    trust = ObservabilityTrustVerdict(verdict=TrustVerdict.TRUSTED, factors={})
    builder.register_manifest(ObservabilityArtifactManifest(manifest_id="m1", telemetry_refs=[], trust_verdict=trust))
    assert builder.get_manifest("m1").trust_verdict.verdict == TrustVerdict.TRUSTED
