# Mock implementation
class ObservabilityAlerts:
    pass

class FeatureObservabilityAlerts:
    def __init__(self):
        self.alerts = [
            "feature_leakage_detected",
            "runtime_feature_skew_elevated",
            "point_in_time_violation",
            "stale_feature_surface_critical",
            "feature_integrity_degraded",
            "dataset_contract_missing_for_candidate"
        ]
