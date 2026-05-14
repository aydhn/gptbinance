class PolicyEvaluation:
    def enforce_decision_quality_evidence(self):
        pass
    def __init__(self, authz_context):
        self.authz_context = authz_context
        self.telemetry_evidence_obligations = []

    def evaluate_security(self, exposed_credentials_active: bool = False):
        if exposed_credentials_active:
             self.authz_context["security_review_required"] = True
             self.telemetry_evidence_obligations.append("security_evidence")
