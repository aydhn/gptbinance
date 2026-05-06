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
