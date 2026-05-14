CAPACITY_ALERTS = [
    "quota_exhaustion_detected",
    "saturation_critical_detected",
    "queue_starvation_detected",
    "noisy_neighbor_detected",
    "emergency_shedding_active",
    "capacity_review_required"
]



# Cost plane evaluation integration
def append_cost_alerts(families):
    families.extend(["budget_guardrail_breached", "vendor_spend_spike_detected"])
    return families
