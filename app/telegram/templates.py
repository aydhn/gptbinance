CAPACITY_TEMPLATES = [
    "capacity_manifest_ready",
    "quota_exhaustion_detected",
    "saturation_critical_detected",
    "emergency_shedding_active",
    "capacity_review_required",
    "capacity_summary_digest"
]



# Cost plane evaluation integration
def append_cost_telegram_templates(templates):
    templates.extend(["cost_manifest_ready", "budget_guardrail_breached"])
    return templates
