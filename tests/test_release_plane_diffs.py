import pytest
from app.release_plane.diffs import ReleaseDiffEngine
from app.release_plane.models import ReleaseCandidate, ReleaseDefinition, ReleaseBundle
from app.release_plane.enums import ReleaseClass, CandidateClass, BundleClass
from datetime import datetime, timezone

def test_diff_engine():
    engine = ReleaseDiffEngine()

    def1 = ReleaseDefinition(release_id="r-1", objective="x", release_class=ReleaseClass.STRATEGY_BUNDLE)
    def2 = ReleaseDefinition(release_id="r-2", objective="y", release_class=ReleaseClass.RISK_CONTROL_BUNDLE)
    bundle = ReleaseBundle(bundle_id="b-1", bundle_class=BundleClass.STANDARD, bundle_hash="123")

    cand = ReleaseCandidate(
        candidate_id="c-1", definition=def2, bundle=bundle,
        candidate_class=CandidateClass.RELEASE_TRAIN_CANDIDATE, created_at=datetime.now(timezone.utc), readiness_class="r"
    )

    diff = engine.compare(cand, def1)
    assert any("Class changed" in s for s in diff.semantic_summaries)
