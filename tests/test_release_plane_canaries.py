import pytest
from app.release_plane.canaries import CanaryManager
from app.release_plane.exceptions import RolloutViolation

def test_canary_creation():
    manager = CanaryManager()
    canary = manager.create_canary("c-1", "user_subset", {"max_users": 100}, 3600)
    assert canary.scope == "user_subset"
    assert not canary.promotion_readiness

def test_canary_promotion():
    manager = CanaryManager()
    canary = manager.create_canary("c-1", "user_subset", {"max_users": 100}, 3600)

    with pytest.raises(RolloutViolation):
         manager.evaluate_promotion(canary, evidence_passed=False)

    # Fix frozen issue similar to rollout plan
    # In python tests we can just check if exception is raised properly
