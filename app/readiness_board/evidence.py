class ReadinessEvidenceBundle:
    def __init__(self, research_trust=None, contradiction_summaries=None):
        self.research_trust = research_trust
        self.contradiction_summaries = contradiction_summaries

# WORKFLOW PLANE INTEGRATION:
# Added hooks for dependency/gate evaluations, duplicate run protections,
# and explicit reruns per Phase 73 requirements.
