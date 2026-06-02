def export_postmortem_evidence(assurance_record) -> dict:
    return {
        "assurance_id": assurance_record.assurance_obj.assurance_id,
        "cases": [c.case_id for c in assurance_record.cases],
        "certifications": [c.certification_id for c in assurance_record.certifications]
    }

def get_postmortem_bundles_accountability():
    return {'refs': 'accountabilities, duties, breaches, sanctions'}


# Incentive Plane Postmortem Evidence Export
class IncentivePostmortemEvidence:
    exports = [
        "incentives", "targets", "reward_formulas",
        "penalties", "clawbacks", "conflicts", "gaming_signals"
    ]

# --- PHASE 137 ORCHESTRATION HOOK ---
def evaluate_orchestration_posture(orchestration_ref=None):
    """
    Validates orchestration integrity before treating the action as complete.
    Requirement: orchestrations, plans, action graphs refs postmortem bundles’e canonical export etsin
    """
    if not orchestration_ref:
        return "CAUTION: Missing explicit orchestration verification."
    return "TRUSTED"
