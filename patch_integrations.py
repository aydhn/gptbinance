import os

def append_to_file(filepath, content):
    if not os.path.exists(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(content + "\n")
    else:
        with open(filepath, 'a') as f:
            f.write("\n" + content + "\n")
    print(f"Patched {filepath}")

# 74. app/accountability_plane/sanctions.py
append_to_file('app/accountability_plane/sanctions.py', """
# Incentive Plane Integration
class SanctionsIncentiveIntegration:
    incentive_plane_deterrence_strength: str = "undefined"
    symbolic_sanction_risk: bool = False
    clawback_refs: list = []

def sanction_applied_treated_behavior_correcting():
    # without incentive evidence explicit caution
    return {"caution": "sanction applied treated behavior-correcting without incentive evidence"}
""")

# 75. app/assurance_plane/surveillance.py
append_to_file('app/assurance_plane/surveillance.py', """
# Incentive Plane Integration
class SurveillanceDiligenceIncentiveIntegration:
    surveillance_incentive_refs: list = []
    under_reporting_hazard_refs: list = []

def surveillance_active_treated_aligned():
    return {"caution": "surveillance active treated aligned without incentive posture"}
""")

# 76. app/immunity_plane/revalidation.py
append_to_file('app/immunity_plane/revalidation.py', """
# Incentive Plane Integration
class RevalidationIncentiveIntegration:
    revalidation_incentive_refs: list = []
    stale_protection_penalty_refs: list = []

def revalidation_passed_treated_durably_motivated():
    return {"caution": "revalidation passed treated durably motivated without incentive basis"}
""")

# 77. app/adaptation_plane/verification.py
append_to_file('app/adaptation_plane/verification.py', """
# Incentive Plane Integration
class VerificationIncentiveIntegration:
    anti_patch_theater_incentive_refs: list = []

def verified_adaptation_treated_alignment_safe():
    return {"caution": "verified adaptation treated alignment-safe without incentive map"}
""")

# 78. app/drift_plane/escalations.py
append_to_file('app/drift_plane/escalations.py', """
# Incentive Plane Integration
class DriftEscalationIncentiveIntegration:
    escalation_incentives_refs: list = []
    suppression_hazards_refs: list = []

def escalation_timely_claimed_while_suppression_active():
    return {"caution": "escalation timely claimed while suppression incentive active"}
""")

# 79. app/normalization_plane/limit_lifts.py
append_to_file('app/normalization_plane/limit_lifts.py', """
# Incentive Plane Integration
class LimitLiftIncentiveIntegration:
    speed_vs_safety_incentive_refs: list = []

def safe_limit_lift_claim_under_speed_biased_reward():
    return {"caution": "safe limit-lift claim under speed-biased reward posture"}
""")

# 80. app/recovery_plane/finalization.py
append_to_file('app/recovery_plane/finalization.py', """
# Incentive Plane Integration
class RecoveryFinalizationIncentiveIntegration:
    residual_harm_concealment_hazard_refs: list = []

def recovery_finalized_treated_honest_under_concealment():
    return {"caution": "recovery finalized treated honest under concealment incentive"}
""")

# 81. app/settlement_plane/fullfinal.py
append_to_file('app/settlement_plane/fullfinal.py', """
# Incentive Plane Integration
class SettlementFullFinalIncentiveIntegration:
    closure_bonus_incentive_refs: list = []
    restitution_gap_incentive_refs: list = []

def full_final_asserted_under_premature_closure_reward():
    return {"caution": "full-final asserted under premature-closure reward posture"}
""")

# 82. app/enforcement_plane/lift.py
append_to_file('app/enforcement_plane/lift.py', """
# Incentive Plane Integration
class EnforcementLiftIncentiveIntegration:
    approval_friction_refs: list = []
    override_speed_reward_refs: list = []

def lift_granted_while_override_for_speed_incentive_active():
    return {"caution": "lift granted while override-for-speed incentive active"}
""")

# 83. app/rights_plane/remedy.py
append_to_file('app/rights_plane/remedy.py', """
# Incentive Plane Integration
class RemedyIncentiveIntegration:
    beneficiary_safe_incentive_refs: list = []
    reporting_incentive_refs: list = []

def remedy_safe_asserted_under_beneficiary_blind_reward():
    return {"caution": "remedy safe asserted under beneficiary-blind reward posture"}
""")

# 84. app/liability_plane/consequences.py
append_to_file('app/liability_plane/consequences.py', """
# Incentive Plane Integration
class LiabilityConsequencesIncentiveIntegration:
    externality_incentive_refs: list = []
    risk_transfer_incentive_refs: list = []

def liability_consequence_hidden_under_local_optimization():
    return {"caution": "liability consequence hidden under local-optimization reward"}
""")

# 85. app/authority_plane/approval.py
append_to_file('app/authority_plane/approval.py', """
# Incentive Plane Integration
class AuthorityApprovalIncentiveIntegration:
    incentive_plane_authority_refs: list = []

def incentive_action_by_actor_lacking_authority():
    return {"caution": "incentive action by actor lacking formula or clawback authority"}
""")

# 86. app/finality_plane/final.py
append_to_file('app/finality_plane/final.py', """
# Incentive Plane Integration
class FinalityIncentiveIntegration:
    no_active_gaming_refs: list = []
    no_unresolved_conflict_refs: list = []
    clawback_posture_refs: list = []

def final_label_under_active_incentive_conflict():
    return {"caution": "final label under active incentive conflict"}
""")

# 87. app/representation_plane/disclosures.py
append_to_file('app/representation_plane/disclosures.py', """
# Incentive Plane Integration
class RepresentationDisclosuresIncentiveIntegration:
    canonical_meanings_refs: list = []

def performance_represented_as_aligned_while_reward_hacking():
    return {"caution": "performance represented as aligned while reward-hacking signals active"}
""")

# 88. app/epistemic_plane/claims.py
append_to_file('app/epistemic_plane/claims.py', """
# Incentive Plane Integration
class EpistemicClaimsIncentiveIntegration:
    incentive_plane_evidence_refs: list = []

def incentive_sounding_claim_without_basis():
    return {"caution": "incentive-sounding claim without subject/target/formula/gaming basis"}
""")

# 89 & 90. app/observability_plane/events.py & diagnostics.py
append_to_file('app/observability_plane/events.py', """
# Incentive Plane Integration
INCENTIVE_EVENTS = [
    "incentive_target_defined",
    "reward_formula_published",
    "reward_issued",
    "penalty_applied",
    "clawback_triggered",
    "incentive_conflict_detected",
    "gaming_signal_detected",
    "incentive_recalibrated"
]
""")

append_to_file('app/observability_plane/diagnostics.py', """
# Incentive Plane Integration
INCENTIVE_DIAGNOSTIC_SIGNALS = [
    "reward_hacking",
    "metric_chasing",
    "escalation_suppression",
    "local_optimization",
    "symbolic_penalty"
]

def payout_count_validation():
    # payout count alone incentive truth yerine gecmesin
    return False
""")

# 91. app/policy_plane/evaluations.py
append_to_file('app/policy_plane/evaluations.py', """
# Incentive Plane Integration
class PolicyIncentiveEvaluations:
    @staticmethod
    def generate_incentive_evidence_obligations(action_risk):
        if action_risk == "high":
            return ["incentive_evidence_required"]
        return []

    @staticmethod
    def review_policy(context):
        if "gameable_target" in context or "hidden_conflict" in context or "symbolic_penalty" in context or "missing_clawback" in context:
            return "deny"
        return "allow"
""")

# 92 & 93. app/policy_kernel/context.py & invariants.py
append_to_file('app/policy_kernel/context.py', """
# Incentive Plane Context Extension
class IncentivePolicyContext:
    incentive_posture: str = "unknown"
    active_conflicts: list = []
    gaming_exposure: list = []
    clawback_status: str = "unknown"
    beneficiary_cost_burden: list = []
""")

append_to_file('app/policy_kernel/invariants.py', """
# Incentive Plane Invariants
INCENTIVE_INVARIANTS = [
    "no trusted high-risk closure, settlement, discharge, final-safe or behavior-aligned claim may be emitted while material incentive treatment remains unresolved in eligible scopes",
    "no subject, target, reward, penalty, friction, clawback, escalation or recalibration event may alter an incentive posture beyond its explicit domain, beneficiary, authority, scope and jurisdiction boundaries",
    "no posture may be treated as aligned, deterrent, risk-adjusted or beneficiary-safe without explicit target integrity, formula rigor, gaming/conflict visibility, friction sufficiency and externality analysis",
    "no contractual, rights-safe, liability-safe, remedy-safe, final-safe or compliance-safe claim may stand while the governing incentive remains materially gameable, conflict-bearing, beneficiary-costly, symbolic or clawback-deficient"
]
""")

# 94 & 95. app/readiness_board/evidence.py & domains.py
append_to_file('app/readiness_board/evidence.py', """
# Incentive Plane Readiness Evidence
INCENTIVE_READINESS_EVIDENCE = [
    "incentive_trust",
    "target_clarity",
    "formula_integrity",
    "gaming_visibility",
    "conflict_visibility",
    "beneficiary_cost_boundedness"
]

def check_incentive_integrity_failures():
    return {"blocker": "critical incentive integrity failures"}
""")

append_to_file('app/readiness_board/domains.py', """
# Incentive Plane Readiness Domain
class IncentiveIntegrityDomain:
    name = "incentive_integrity"
    factors = [
        "target_clarity",
        "formula_integrity",
        "gaming_visibility",
        "conflict_visibility",
        "beneficiary_cost_boundedness"
    ]
""")

# 96 & 97. app/reliability/domains.py & slos.py
append_to_file('app/reliability/domains.py', """
# Incentive Plane Reliability Domain
class IncentiveReliabilityDomain:
    name = "incentive_integrity"
    inputs = [
        "reward_hacking",
        "concealment_incentive",
        "symbolic_penalties",
        "hidden_conflicts"
    ]
""")

append_to_file('app/reliability/slos.py', """
# Incentive Plane Reliability SLOs
INCENTIVE_SLOS = {
    "unresolved_material_gaming_ceiling": 0,
    "hidden_conflict_absence": True,
    "symbolic_penalty_absence": True,
    "missing_clawback_absence": True,
    "trusted_incentive_degraded_ratio": 0.05
}
""")

# 98 & 99. app/postmortem_plane/contributors.py & evidence.py
append_to_file('app/postmortem_plane/contributors.py', """
# Incentive Plane Contributors
INCENTIVE_CONTRIBUTORS = [
    "reward_hacking",
    "hidden_conflict",
    "symbolic_penalty",
    "escalation_suppression",
    "beneficiary_blind_efficiency",
    "local_optimization_externality"
]
""")

append_to_file('app/postmortem_plane/evidence.py', """
# Incentive Plane Postmortem Evidence Export
class IncentivePostmortemEvidence:
    exports = [
        "incentives", "targets", "reward_formulas",
        "penalties", "clawbacks", "conflicts", "gaming_signals"
    ]
""")

# 100 & 101. app/evidence_graph/artefacts.py & packs.py
append_to_file('app/evidence_graph/artefacts.py', """
# Incentive Plane Evidence Artefacts
INCENTIVE_ARTEFACT_FAMILIES = [
    "incentives", "subjects", "targets", "levers",
    "rewards", "reward_formulas", "delayed_rewards",
    "penalties", "penalty_triggers", "frictions", "clawbacks",
    "escalation", "surveillance", "shared", "conflicts",
    "moral_hazard", "externalities", "gaming", "reviews",
    "recalibration", "comparisons", "equivalence", "trust_reports"
]

INCENTIVE_RELATIONS = [
    "incentivized_by",
    "rewarded_under",
    "penalized_under",
    "clawed_back_by",
    "conflicted_by",
    "gamed_under",
    "diverged_incentive_from"
]
""")

append_to_file('app/evidence_graph/packs.py', """
# Incentive Plane Evidence Packs
INCENTIVE_EVIDENCE_PACKS = [
    "incentive_integrity_pack",
    "subject_target_review_pack",
    "reward_penalty_review_pack",
    "conflict_gaming_review_pack"
]
""")

# 102. app/reviews/requests.py
append_to_file('app/reviews/requests.py', """
# Incentive Plane Reviews
INCENTIVE_REVIEW_CLASSES = [
    "incentive_integrity_review",
    "subject_target_review",
    "reward_penalty_review",
    "friction_clawback_review",
    "conflict_gaming_review",
    "beneficiary_cost_review"
]
""")

# 103. app/identity/capabilities.py
append_to_file('app/identity/capabilities.py', """
# Incentive Plane Capabilities
INCENTIVE_CAPABILITIES = [
    "inspect_incentive_manifest",
    "review_subjects_targets_and_levers",
    "review_rewards_penalties_and_clawbacks",
    "review_conflicts_gaming_and_externalities",
    "review_alignment_and_beneficiary_costs"
]
""")

# 104 & 105. app/observability/alerts.py & runbooks.py
append_to_file('app/observability/alerts.py', """
# Incentive Plane Alerts
INCENTIVE_ALERTS = [
    "gaming_signal_detected",
    "hidden_conflict_detected",
    "symbolic_penalty_detected",
    "beneficiary_cost_spike_detected",
    "clawback_gap_detected",
    "incentive_review_required"
]
""")

append_to_file('app/observability/runbooks.py', """
# Incentive Plane Runbooks
INCENTIVE_RUNBOOKS = [
    "target_integrity_review",
    "formula_gaming_review",
    "conflict_resolution_review",
    "clawback_reassessment",
    "beneficiary_cost_review",
    "incentive_drift_cleanup_review"
]
""")

# 106 & 107. app/telegram/notifier.py & templates.py
append_to_file('app/telegram/notifier.py', """
# Incentive Plane Notifier Support
INCENTIVE_NOTIFIER_EVENTS = [
    "incentive_manifest_ready",
    "gaming_signal_detected",
    "hidden_conflict_detected",
    "beneficiary_cost_spike_detected",
    "incentive_review_required"
]
""")

append_to_file('app/telegram/templates.py', """
# Incentive Plane Telegram Templates
INCENTIVE_TEMPLATES = {
    "incentive_manifest_ready": "Incentive manifest ready.",
    "gaming_signal_detected": "Gaming signal detected.",
    "hidden_conflict_detected": "Hidden conflict detected.",
    "beneficiary_cost_spike_detected": "Beneficiary cost spike detected.",
    "incentive_review_required": "Incentive review required.",
    "incentive_summary_digest": "Incentive summary digest."
}
""")

# 108. app/main.py modifications
import sys

def patch_main():
    main_file = 'app/main.py'
    if not os.path.exists(main_file):
        return

    with open(main_file, 'r') as f:
        content = f.read()

    if "show-incentive-registry" in content:
        print("app/main.py already patched.")
        return

    # Find the parser = argparse.ArgumentParser...
    insert_str = """
    parser.add_argument("--show-incentive-registry", action="store_true", help="Show canonical Incentive Registry")
    parser.add_argument("--show-incentive-object", action="store_true")
    parser.add_argument("--incentive-id", type=str)
    parser.add_argument("--show-incentives", action="store_true")
    parser.add_argument("--show-incentive-subjects", action="store_true")
    parser.add_argument("--show-behavioral-targets", action="store_true")
    parser.add_argument("--show-incentive-levers", action="store_true")
    parser.add_argument("--show-rewards", action="store_true")
    parser.add_argument("--show-reward-formulas", action="store_true")
    parser.add_argument("--show-delayed-rewards", action="store_true")
    parser.add_argument("--show-penalties", action="store_true")
    parser.add_argument("--show-penalty-triggers", action="store_true")
    parser.add_argument("--show-friction-controls", action="store_true")
    parser.add_argument("--show-clawbacks", action="store_true")
    parser.add_argument("--show-escalation-incentives", action="store_true")
    parser.add_argument("--show-surveillance-incentives", action="store_true")
    parser.add_argument("--show-shared-incentives", action="store_true")
    parser.add_argument("--show-incentive-conflicts", action="store_true")
    parser.add_argument("--show-moral-hazard", action="store_true")
    parser.add_argument("--show-externalities", action="store_true")
    parser.add_argument("--show-gaming-signals", action="store_true")
    parser.add_argument("--show-incentive-reviews", action="store_true")
    parser.add_argument("--show-incentive-recalibration", action="store_true")
    parser.add_argument("--show-incentive-comparisons", action="store_true")
    parser.add_argument("--show-incentive-readiness", action="store_true")
    parser.add_argument("--show-incentive-forecast", action="store_true")
    parser.add_argument("--show-incentive-debt", action="store_true")
    parser.add_argument("--show-incentive-equivalence", action="store_true")
    parser.add_argument("--show-incentive-trust", action="store_true")
    parser.add_argument("--show-incentive-review-packs", action="store_true")
"""

    # Simple replace logic
    content = content.replace('args = parser.parse_args()', insert_str + '\n    args = parser.parse_args()')

    insert_handler = """
    elif args.show_incentive_registry:
        print("[CLI] Initializing and displaying canonical Incentive Registry...")
    elif args.show_incentive_object and args.incentive_id:
        print(f"[CLI] Showing details for Incentive ID: {args.incentive_id}")
    elif args.show_incentive_trust:
        print(f"[CLI] Evaluating Trust Verdict for Incentive IDs...")
"""

    content = content.replace('else:', insert_handler + '    else:')

    with open(main_file, 'w') as f:
        f.write(content)
    print("Patched app/main.py")

patch_main()
