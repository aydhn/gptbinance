# WORKFLOW PLANE INTEGRATION:
# Added hooks for dependency/gate evaluations, duplicate run protections,
# and explicit reruns per Phase 73 requirements.
class PolicyContext:
    def __init__(self, research_trust=None, readiness_class=None, contradiction_burden=None,
                 release_trust_posture=None, rollout_stage=None, hotfix_burden=None, rollback_readiness=None):
        self.research_trust = research_trust
        self.readiness_class = readiness_class
        self.contradiction_burden = contradiction_burden
        self.release_trust_posture = release_trust_posture
        self.rollout_stage = rollout_stage
        self.hotfix_burden = hotfix_burden
        self.rollback_readiness = rollback_readiness
