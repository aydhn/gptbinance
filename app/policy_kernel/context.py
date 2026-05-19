def enrich_policy_context_with_learning(context: dict) -> dict:
    # learning posture, known failure classes, stale lessons, recurrence burden ve hardening validation gaps
    context["learning_sufficiency"] = "trusted"
    return context


# -- Learning Plane Additions --
def enrich_policy_context_with_learning(context: dict) -> dict:
    context["learning_sufficiency"] = "trusted"
    return context
