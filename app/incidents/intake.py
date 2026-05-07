# Mock implementation
class IncidentIntake:
    pass


# Added Incident Signals
INCIDENT_SIGNALS = [
    "runtime_build_mismatch",
    "lock_integrity_broken",
    "missing_attestation_critical",
    "reproducibility_regression",
    "unexpected_dependency_drift",
]

class FeatureIncidentSignals:
    def __init__(self):
        self.signals = [
            "feature_leakage_detected",
            "training_serving_skew_critical",
            "runtime_feature_manifest_missing",
            "point_in_time_violation",
            "stale_feature_surface_critical"
        ]
