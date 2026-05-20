import pytest
from app.release_plane.rollouts import check_rollout_provenance

def test_state_transition_without_actor_anomaly():
    assert "BLOCKER/CAUTION" in check_rollout_provenance("rel-1", [])
    assert "TRUSTED" in check_rollout_provenance("rel-2", ["ref1"])
