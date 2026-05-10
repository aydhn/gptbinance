import pytest
from app.release_plane.manifests import ManifestBuilder
from app.release_plane.models import ReleaseCandidate, ReleaseDefinition, ReleaseBundle, ReleaseBundleEntry, BundlePin
from app.release_plane.enums import ReleaseClass, CandidateClass, BundleClass
from app.release_plane.exceptions import ReleasePlaneError
from datetime import datetime, timezone

def test_manifest_builder():
    builder = ManifestBuilder()

    definition = ReleaseDefinition(release_id="rel-1", objective="x", release_class=ReleaseClass.STRATEGY_BUNDLE)
    bundle = ReleaseBundle(
        bundle_id="bnd-1", bundle_class=BundleClass.STANDARD, bundle_hash="abc",
        entries=[
            ReleaseBundleEntry(
                entry_id="e-1", entry_type="t", manifest_ref="m",
                pins=[BundlePin(artifact_id="1", version_hash="abc", pin_type="t")]
            )
        ]
    )

    candidate = ReleaseCandidate(
        candidate_id="c-1", definition=definition, bundle=bundle,
        candidate_class=CandidateClass.RELEASE_TRAIN_CANDIDATE, created_at=datetime.now(timezone.utc),
        readiness_class="ready"
    )

    manifest = builder.build_manifest(candidate)
    assert manifest.bundle_hash == "abc"
    assert len(manifest.pins) == 1
