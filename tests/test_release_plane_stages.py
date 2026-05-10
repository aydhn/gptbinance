import pytest
from app.release_plane.stages import StageManager
from app.release_plane.exceptions import RolloutViolation

def test_valid_transitions():
    StageManager.validate_transition("candidate_prepared", "canary_active")
    StageManager.validate_transition("canary_active", "probationary_active")
    StageManager.validate_transition("probationary_active", "expansion_pending")
    StageManager.validate_transition("expansion_pending", "live_full_active")

def test_invalid_transition():
    with pytest.raises(RolloutViolation):
         StageManager.validate_transition("candidate_prepared", "live_full_active")
