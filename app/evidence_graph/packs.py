CAPACITY_PACKS = [
    "capacity_integrity_pack",
    "saturation_backpressure_review_pack",
    "reservation_fairness_review_pack",
    "quota_exhaustion_review_pack"
]



# Cost plane evaluation integration
def append_cost_packs(packs):
    packs.extend(["cost_integrity_pack", "allocation_review_pack", "budget_guardrail_review_pack"])
    return packs
