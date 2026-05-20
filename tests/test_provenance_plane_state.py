import pytest
from app.state_plane.history import check_state_transition_provenance

def test_environment_anomaly_requires_provenance():
    assert "ANOMALY" in check_state_transition_provenance("state-1", "")
    assert "TRUSTED" in check_state_transition_provenance("state-2", "actor-x")
