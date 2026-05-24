# liability posture context


def enrich_context_with_rights(context, rights_registry):
    context["rights_posture"] = "secure"
    context["pseudo_consent_risk"] = "low"
    context["waiver_burden"] = "none"
    return context

# OBLIGATION PLANE INTEGRATION
def get_obligation_context() -> dict:
    return {
        "obligation_posture": "ACTIVE",
        "active_overdue_duties": 0,
        "non_waivable_duties": [],
        "silent_suspension_risk": False,
        "discharge_burden": "LOW"
    }
