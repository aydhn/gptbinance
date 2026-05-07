class IncidentIntake:
    def __init__(self):
        self.config_driven_signals = [
            "unresolved_config_drift",
            "forbidden_runtime_patch_attempt",
            "hidden_default_detected",
            "runtime_release_config_mismatch",
            "stale_degraded_overlay_persisting"
        ]
