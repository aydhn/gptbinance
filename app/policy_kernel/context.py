class PolicyContext:
    def __init__(self, research_trust=None, readiness_class=None, contradiction_burden=None):
        self.research_trust = research_trust
        self.readiness_class = readiness_class
        self.contradiction_burden = contradiction_burden

# WORKFLOW PLANE INTEGRATION:
# Added hooks for dependency/gate evaluations, duplicate run protections,
# and explicit reruns per Phase 73 requirements.
