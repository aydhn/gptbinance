class PolicyEvaluation:
    def __init__(self, authz_context):
        self.authz_context = authz_context
        self.telemetry_evidence_obligations = []
