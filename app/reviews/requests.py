# Mock implementation
class ReviewRequests:
    pass

class FeatureReviewClasses:
    def __init__(self):
        self.classes = [
            "feature_leakage_review",
            "dataset_contract_review",
            "runtime_feature_equivalence_review",
            "skew_review",
            "hidden_transform_review"
        ]
