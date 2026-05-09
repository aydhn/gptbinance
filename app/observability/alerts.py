class AlertRule:
    RESEARCH_TRUST_DEGRADED = "research_trust_degraded"
    CRITICAL_RESEARCH_OVERLAP = "critical_research_overlap_detected"

# WORKFLOW PLANE INTEGRATION:
# Added hooks for dependency/gate evaluations, duplicate run protections,
# and explicit reruns per Phase 73 requirements.
