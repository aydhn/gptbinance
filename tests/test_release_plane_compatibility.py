import pytest
from app.release_plane.compatibility import StandardCompatibilityEvaluator
from app.release_plane.models import ReleaseCandidate, ReleaseDefinition, ReleaseBundle, ReleaseBundleEntry, BundlePin, EnvironmentTarget
from app.release_plane.enums import ReleaseClass, BundleClass, EnvironmentClass, CandidateClass
from datetime import datetime, timezone

def test_compatibility_pass():
    evaluator = StandardCompatibilityEvaluator()
    target_env = EnvironmentTarget(environment_class=EnvironmentClass.REPLAY)

    definition = ReleaseDefinition(
        release_id="rel-1", objective="x", release_class=ReleaseClass.STRATEGY_BUNDLE,
        target_environments=[target_env]
    )

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

    report = evaluator.evaluate(candidate, target_env)
    assert report.is_compatible is True

def test_compatibility_fail_missing_pins():
    evaluator = StandardCompatibilityEvaluator()
    target_env = EnvironmentTarget(environment_class=EnvironmentClass.REPLAY)

    definition = ReleaseDefinition(
        release_id="rel-2", objective="x", release_class=ReleaseClass.STRATEGY_BUNDLE,
        target_environments=[target_env]
    )

    bundle = ReleaseBundle(
        bundle_id="bnd-2", bundle_class=BundleClass.STANDARD, bundle_hash="abc",
        entries=[
            ReleaseBundleEntry(
                entry_id="e-2", entry_type="t", manifest_ref="m",
                pins=[] # Missing pins
            )
        ]
    )

    candidate = ReleaseCandidate(
        candidate_id="c-2", definition=definition, bundle=bundle,
        candidate_class=CandidateClass.RELEASE_TRAIN_CANDIDATE, created_at=datetime.now(timezone.utc),
        readiness_class="ready"
    )

    report = evaluator.evaluate(candidate, target_env)
    assert report.is_compatible is False
    assert any("Missing dependency blockers" in str(b) for b in report.blockers)
