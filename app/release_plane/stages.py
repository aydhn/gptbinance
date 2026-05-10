from app.release_plane.exceptions import RolloutViolation

# Valid stage transitions map
VALID_TRANSITIONS = {
    "candidate_prepared": ["candidate_held", "canary_active", "retired_release"],
    "candidate_held": ["candidate_prepared", "retired_release"],
    "canary_active": ["canary_paused", "probationary_active", "rollback_pending"],
    "canary_paused": ["canary_active", "rollback_pending"],
    "probationary_active": ["expansion_pending", "rollback_pending", "superseded"],
    "expansion_pending": ["probationary_active", "live_full_active", "rollback_pending"],
    "live_full_active": ["rollback_pending", "superseded"],
    "rollback_pending": ["retired_release"],
    "superseded": [],
    "retired_release": []
}

class StageManager:
    @staticmethod
    def validate_transition(current_stage: str, target_stage: str) -> None:
        if current_stage not in VALID_TRANSITIONS:
             raise RolloutViolation(f"Unknown current stage: {current_stage}")

        if target_stage not in VALID_TRANSITIONS[current_stage]:
             raise RolloutViolation(f"Invalid transition from {current_stage} to {target_stage}. No hidden state jumps allowed.")
