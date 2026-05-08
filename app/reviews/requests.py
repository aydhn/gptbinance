class ReviewRequests:
    def request_review(self, review_class: str, metadata: dict):
        # allocation_integrity_review, sleeve_budget_review, allocation_equivalence_review
        pass

class ExecutionReviewClasses:
    CLASSES = [
        "execution_integrity_review",
        "venue_filter_review",
        "slippage_cluster_review",
        "cancel_replace_review",
        "execution_equivalence_review",
        "aggressive_routing_review"
    ]
