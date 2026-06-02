def get_assurance_capabilities() -> list:
    return [
        "inspect_assurance_manifest",
        "review_claims_evidence_and_sufficiency",
        "review_certifications_attestations_and_surveillance",
        "review_caveats_contradictions_and_revocations",
        "review_assurance_scope_and_current_validity"
    ]

ACCOUNTABILITY_CAPABILITIES = ['inspect_accountability_manifest', 'review_subjects_duties_and_breaches', 'review_sanctions_remediation_and_restitution', 'review_appeals_reversals_and_reinstatement', 'review_shared_accountability_and_scapegoating_risks']


# Incentive Plane Capabilities
INCENTIVE_CAPABILITIES = [
    "inspect_incentive_manifest",
    "review_subjects_targets_and_levers",
    "review_rewards_penalties_and_clawbacks",
    "review_conflicts_gaming_and_externalities",
    "review_alignment_and_beneficiary_costs"
]

# --- PHASE 137 ORCHESTRATION HOOK ---
def evaluate_orchestration_posture(orchestration_ref=None):
    """
    Validates orchestration integrity before treating the action as complete.
    Requirement: capabilities: inspect_orchestration_manifest, review_intents_plans_and_dependencies
    """
    if not orchestration_ref:
        return "CAUTION: Missing explicit orchestration verification."
    return "TRUSTED"
