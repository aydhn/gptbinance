class IncidentIntake:
    RESEARCH_OVERLAP = "critical_research_overlap_detected"
    CONTRADICTION_BURST = "unresolved_contradiction_burst"
    SELECTIVE_EVIDENCE = "selective_evidence_pattern_detected"

# WORKFLOW PLANE INTEGRATION:
# Added hooks for dependency/gate evaluations, duplicate run protections,
# and explicit reruns per Phase 73 requirements.
