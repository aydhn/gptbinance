class AccountabilityDuty:
    meta_governance_duty_canon_lineage_ref: str = None


def validate_stewardship_duties(context):
    """
    Integration for Stewardship Plane.
    Rule: Must include preservation and handoff duties refs.
    If absent, generates an explicit caution.
    """
    if "stewardship_evidence" not in context:
        return "CAUTION: Action treated safe without explicit stewardship evidence."
    return "TRUSTED"
