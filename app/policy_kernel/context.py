def build_capacity_policy_context():
    pass



# Cost plane evaluation integration
def append_cost_context(context):
    context["budget_posture"] = "ok"
    context["guardrail_breaches"] = []
    context["cost_debt"] = 0
    return context
