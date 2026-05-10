import pytest
from app.release_plane.rollouts import GovernanceRolloutEvaluator
from app.release_plane.models import ReleaseCandidate, ReleaseDefinition, ReleaseBundle
from app.release_plane.enums import ReleaseClass, BundleClass, CandidateClass
from app.release_plane.exceptions import RolloutViolation
from datetime import datetime, timezone

def test_rollout_stage_progression():
    evaluator = GovernanceRolloutEvaluator()
    definition = ReleaseDefinition(release_id="rel-1", objective="x", release_class=ReleaseClass.STRATEGY_BUNDLE)
    bundle = ReleaseBundle(bundle_id="b", bundle_class=BundleClass.STANDARD, bundle_hash="h")
    candidate = ReleaseCandidate(
        candidate_id="c-1", definition=definition, bundle=bundle,
        candidate_class=CandidateClass.RELEASE_TRAIN_CANDIDATE, created_at=datetime.now(timezone.utc),
        readiness_class="ready"
    )

    plan = evaluator.evaluate(candidate)
    assert plan.current_stage == "candidate_prepared"

    # Valid advance
    plan = evaluator.advance_stage(plan, "canary_active", evidence_approved=True)
    assert plan.current_stage == "canary_active"

    # Missing evidence
    with pytest.raises(RolloutViolation):
        evaluator.advance_stage(plan, "probationary_active", evidence_approved=False)

    # Hidden state jump (canary to full live without probation)
    with pytest.raises(RolloutViolation):
        evaluator.advance_stage(plan, "live_full_active", evidence_approved=True)
