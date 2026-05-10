import pytest
from app.release_plane.bundles import BundleBuilder
from app.release_plane.models import ReleaseBundleEntry, BundlePin
from app.release_plane.enums import BundleClass
from app.release_plane.exceptions import InvalidCandidateBundle

def test_bundle_creation_and_hash():
    builder = BundleBuilder("bnd-123", BundleClass.STANDARD)

    entry = ReleaseBundleEntry(
        entry_id="strat-1",
        entry_type="strategy",
        manifest_ref="man-1",
        pins=[BundlePin(artifact_id="art-1", version_hash="hash-1", pin_type="strategy")]
    )

    builder.add_entry(entry)
    bundle = builder.build()

    assert bundle.bundle_id == "bnd-123"
    assert len(bundle.entries) == 1
    assert bundle.bundle_hash is not None
    assert bundle.bundle_hash != ""

def test_empty_bundle_rejection():
    builder = BundleBuilder("bnd-empty", BundleClass.STANDARD)
    with pytest.raises(InvalidCandidateBundle):
         builder.build()
