class ReviewClass:
    RELEASE_INTEGRITY_REVIEW = "release_integrity_review"
    ROLLOUT_REVIEW = "rollout_review"
    CANARY_REVIEW = "canary_review"
    ROLLBACK_READINESS_REVIEW = "rollback_readiness_review"
    HOTFIX_REVIEW = "hotfix_review"
    RELEASE_EQUIVALENCE_REVIEW = "release_equivalence_review"

class ReviewRequest:
    def attach_release_evidence_suitability_metadata(self):
        pass


class ReviewRequestDispatcher:
    def request_rca_review(self, postmortem_id: str):
        pass
