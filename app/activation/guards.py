class ActivationGuard:
    def require_decision_object(self):
        pass
    def __init__(self, progression_actor_session_id: str, observability_manifest_id: str = None):
        self.progression_actor_session_id = progression_actor_session_id
        self.observability_manifest_id = observability_manifest_id

    def evaluate_security(self, exposed_credential_active: bool, critical_exploitability_active: bool, stale_cert_active: bool, missing_security_evidence: bool):
         if exposed_credential_active or critical_exploitability_active or stale_cert_active or missing_security_evidence:
              raise Exception("Activation blocked due to critical security exposure or lack of trust.")
