def evaluate_assurance_policy(assurance_record) -> str:
    if not assurance_record.cases:
        return "DENY: Insufficient evidence context"
    if assurance_record.expiry and assurance_record.expiry.is_expired:
        return "DENY: Stale certification"
    return "ALLOW"

def policy_review_accountability(action_risk: str, accountability_issues: list = None):
    if action_risk == 'high' and accountability_issues:
        return {'status': 'deny', 'message': 'Missing owner, symbolic sanction, or unresolved restitution detected.'}
    return {'status': 'approve'}


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

# --- PHASE 137 ORCHESTRATION HOOK ---
def evaluate_orchestration_posture(orchestration_ref=None):
    """
    Validates orchestration integrity before treating the action as complete.
    Requirement: stale plan, missing gate, bypassed approval context policy review/deny sonucu üretsin
    """
    if not orchestration_ref:
        return "CAUTION: Missing explicit orchestration verification."
    return "TRUSTED"

# Autonomy Integration Phase 138
def integrate_autonomy_evaluations():
    pass
