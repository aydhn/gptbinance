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
