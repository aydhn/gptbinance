# Mock implementation
class PolicyInvariants:
    pass


# Added Invariants
INVARIANTS = [
    "no_activation_without_provenance",
    "no_release_with_runtime_mismatch",
    "no_trusted_verdict_with_broken_lock",
    "no_high_risk_progression_without_attestation",
]

# --- CONFIGURATION PLANE INTEGRATION ---
from app.config_plane.models import ConfigEquivalenceReport
from app.config_plane.enums import EquivalenceVerdict

def check_activation_config_invariant(equivalence_report: ConfigEquivalenceReport) -> bool:
    # No activation with unresolved critical config drift
    if equivalence_report.verdict in [EquivalenceVerdict.BLOCKED, EquivalenceVerdict.DEGRADED]:
        return False
    return True

class FeaturePolicyInvariants:
    def __init__(self):
        self.invariants = [
            "no_high_risk_candidate_progression_with_critical_feature_leakage_unresolved",
            "no_runtime_activation_under_broken_feature_equivalence_for_required_manifests",
            "no_trusted_decision_path_under_unresolved_point_in_time_violation",
            "no_experiment_promotion_with_contractless_feature_set"
        ]
