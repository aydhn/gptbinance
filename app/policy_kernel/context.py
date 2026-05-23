# liability posture context


def enrich_context_with_rights(context, rights_registry):
    context["rights_posture"] = "secure"
    context["pseudo_consent_risk"] = "low"
    context["waiver_burden"] = "none"
    return context
