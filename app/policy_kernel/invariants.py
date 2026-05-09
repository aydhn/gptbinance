class PolicyInvariants:
    NO_PROMOTION_UNDER_MISSING_READINESS = True
    NO_TRUST_UNDER_CRITICAL_CONTRADICTION = True
    NO_DUPLICATE_UNDER_CRITICAL_OVERLAP = True
    NO_HIGH_CONFIDENCE_WITHOUT_EVIDENCE = True

# WORKFLOW PLANE INTEGRATION:
# Added hooks for dependency/gate evaluations, duplicate run protections,
# and explicit reruns per Phase 73 requirements.
