class ReviewRequests:
    CLASSES = [
        "precedent_integrity_review",
        "holding_rationale_review",
        "analogy_distinction_review",
        "conflict_hierarchy_review",
        "carveout_exception_review",
        "precedent_portability_review"
    ]

# Precedent Plane Integration added

class ReviewRequest:
    def __init__(self):
        self.canonical_review_classes = ['authority_integrity_review', 'mandate_decision_right_review', 'delegation_override_review', 'ratification_legitimacy_review', 'quorum_sod_review', 'authority_portability_review']
        self.authority_plane_evidence_suitability_metadata = None
