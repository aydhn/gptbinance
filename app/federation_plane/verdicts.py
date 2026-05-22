from typing import Dict, Any

class FederationVerdicts:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("partner_evidence_abuse"):
            return {"status": "blocker", "reason": "federated_pass_under_exploitable_partner_evidence"}
        return {"status": "ok"}
