CAPACITY_CAPABILITIES = [
    "inspect_capacity_manifest",
    "review_quota_allocations",
    "approve_emergency_reservation",
    "review_shedding_policy",
    "review_capacity_fairness"
]



# Cost plane evaluation integration
def append_cost_capabilities(capabilities):
    capabilities.extend(["inspect_cost_manifest", "review_allocations", "review_budget_guardrails"])
    return capabilities
