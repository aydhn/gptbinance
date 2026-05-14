CAPACITY_RUNBOOKS = [
    "saturation_investigation",
    "queue_backpressure_review",
    "quota_exhaustion_response",
    "fairness_noisy_neighbor_review",
    "emergency_shedding_review",
    "live_headroom_assessment"
]



# Cost plane evaluation integration
def append_cost_runbooks(refs):
    refs.extend(["spend_spike_investigation", "allocation_attribution_review"])
    return refs
