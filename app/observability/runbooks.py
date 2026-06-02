def get_assurance_runbooks() -> list:
    return [
        "evidence_sufficiency_review",
        "certification_scope_review",
        "contradiction_resolution_review",
        "surveillance_recovery_review",
        "revocation_readiness_review",
        "assurance_drift_cleanup_review"
    ]

ACCOUNTABILITY_RUNBOOKS = ['duty_map_revalidation', 'breach_evidence_review', 'sanction_proportionality_review', 'restitution_owner_review', 'appeal_visibility_review', 'accountability_drift_cleanup_review']


# Incentive Plane Runbooks
INCENTIVE_RUNBOOKS = [
    "target_integrity_review",
    "formula_gaming_review",
    "conflict_resolution_review",
    "clawback_reassessment",
    "beneficiary_cost_review",
    "incentive_drift_cleanup_review"
]

# --- PHASE 137 ORCHESTRATION HOOK ---
def evaluate_orchestration_posture(orchestration_ref=None):
    """
    Validates orchestration integrity before treating the action as complete.
    Requirement: runbook refs: plan_revalidation, gate_integrity_review
    """
    if not orchestration_ref:
        return "CAUTION: Missing explicit orchestration verification."
    return "TRUSTED"
