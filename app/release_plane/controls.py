class ReleaseControl:
    def approve(self, approver_principal_id: str, trust_engine):
        if trust_engine.evaluate_trust(approver_principal_id).verdict != 'trusted':
            raise ValueError("Untrusted principal")
