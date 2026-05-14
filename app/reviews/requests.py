CAPACITY_REVIEWS = [
    "capacity_integrity_review",
    "quota_review",
    "reservation_review",
    "saturation_review",
    "fairness_review",
    "shedding_review"
]



# Cost plane evaluation integration
def append_cost_review_classes(classes):
    classes.extend(["cost_integrity_review", "allocation_review", "budget_guardrail_review"])
    return classes
