import pytest
from app.environment_plane.observations import check_env_observation_provenance

def test_release_anomaly_without_rollout_blocked():
    assert "CAUTION" in check_env_observation_provenance("env-1", [])
    assert "TRUSTED" in check_env_observation_provenance("env-2", ["ref1"])
