class TelegramNotifierEvent:
    RESEARCH_MANIFEST_READY = "research_manifest_ready"
    RESEARCH_TRUST_DEGRADED = "research_trust_degraded"

# WORKFLOW PLANE INTEGRATION:
# Added hooks for dependency/gate evaluations, duplicate run protections,
# and explicit reruns per Phase 73 requirements.
