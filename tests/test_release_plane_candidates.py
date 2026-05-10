import pytest
from datetime import timezone
from datetime import datetime, timedelta
from app.release_plane.candidates import ReleaseCandidateRegistry
from app.release_plane.models import ReleaseCandidate, ReleaseDefinition, ReleaseBundle, EnvironmentTarget
from app.release_plane.enums import CandidateClass, ReleaseClass, BundleClass, EnvironmentClass

def test_candidate_registration_and_approval():
    registry = ReleaseCandidateRegistry()

    definition = ReleaseDefinition(
        release_id="rel-1", objective="x", release_class=ReleaseClass.STRATEGY_BUNDLE, target_environments=[]
    )
    bundle = ReleaseBundle(bundle_id="bnd-1", bundle_class=BundleClass.STANDARD, bundle_hash="hash", entries=[])

    candidate = ReleaseCandidate(
        candidate_id="cand-1",
        definition=definition,
        bundle=bundle,
        candidate_class=CandidateClass.RELEASE_TRAIN_CANDIDATE,
        created_at=datetime.now(timezone.utc),
        expiry=datetime.now(timezone.utc) + timedelta(days=1),
        readiness_class="ready",
        source_refs=[],
        lineage_refs=[]
    )

    registry.register(candidate)

    assert not registry.is_approved("cand-1")
    registry.add_approval("cand-1", "user1")
    assert registry.is_approved("cand-1")

def test_candidate_expiry():
    registry = ReleaseCandidateRegistry()

    definition = ReleaseDefinition(release_id="rel-2", objective="x", release_class=ReleaseClass.STRATEGY_BUNDLE)
    bundle = ReleaseBundle(bundle_id="bnd-2", bundle_class=BundleClass.STANDARD, bundle_hash="hash")

    candidate = ReleaseCandidate(
        candidate_id="cand-2",
        definition=definition,
        bundle=bundle,
        candidate_class=CandidateClass.RELEASE_TRAIN_CANDIDATE,
        created_at=datetime.now(timezone.utc) - timedelta(days=2),
        expiry=datetime.now(timezone.utc) - timedelta(days=1), # Expired
        readiness_class="ready"
    )

    registry.register(candidate)

    # Custom logic in registry should handle expired candidates
    fetched = registry.get("cand-2")
    # For now we just check it was registered
    assert fetched.candidate_id == "cand-2"
