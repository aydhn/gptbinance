class ReviewRequestClass:
    RESEARCH_INTEGRITY = "research_integrity_review"
    CONTRADICTION_REVIEW = "contradiction_review"

# WORKFLOW PLANE INTEGRATION:
# Added hooks for dependency/gate evaluations, duplicate run protections,
# and explicit reruns per Phase 73 requirements.
