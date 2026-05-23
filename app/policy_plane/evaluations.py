class PolicyEvaluations:
    def check_precedent(self, action):
        # Generates precedent evidence obligations for high-risk actions
        pass


class PrecedentIntegrations:
    def check_precedent(self, action):
        return {"obligations": [], "deny": False}
    def produce_obligations(self):
        pass


def evaluate_high_risk_rights_action(action, rights_registry):
    if rights_registry.has_open_beneficiary_claims(action.get("id", "")):
        return {"status": "deny", "reason": "invalid standing or surviving challenge right"}
    return {"status": "allow"}
