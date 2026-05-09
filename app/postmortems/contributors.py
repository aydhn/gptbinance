class PostmortemContributor:
    FAILED_ASSUMPTION = "failed_assumption"
    MISSING_CONTRADICTION = "missing_contradiction"
    DUPLICATED_RESEARCH = "duplicated_research"
    SELECTIVE_EVIDENCE = "selective_evidence"

# WORKFLOW PLANE INTEGRATION:
# Added hooks for dependency/gate evaluations, duplicate run protections,
# and explicit reruns per Phase 73 requirements.
