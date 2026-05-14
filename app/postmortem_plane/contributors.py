CAPACITY_CONTRIBUTORS = [
    "chronic_saturation",
    "stale_reservation",
    "hidden_shared_queue",
    "quota_near_edge_operation",
    "noisy_neighbor_interference",
    "autoscaling_false_comfort"
]



# Cost plane evaluation integration
def append_cost_postmortem_classes(existing_classes):
    existing_classes.extend([
        "hidden_shared_cost_subsidy",
        "stale_reservation_waste",
        "unit_economics_blind_spot",
        "quota_spend_cliff",
        "retry_amplification_cost_leak",
        "cheapness_driven_reliability_erosion"
    ])
    return existing_classes
