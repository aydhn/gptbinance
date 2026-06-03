class ReviewRequests:
    pass

def request_resilience_review(review_type):
    canonical_reviews = ["resilience_integrity_review", "shock_margin_review", "graceful_containment_review", "reserve_recovery_review", "beneficiary_surge_review", "hidden_fragility_review"]
    if review_type in canonical_reviews:
        return {"status": "requested", "type": review_type}
    return {"status": "error"}
