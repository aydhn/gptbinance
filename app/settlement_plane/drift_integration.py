from typing import Dict, Any


class DriftIntegrationLinkage:
    @staticmethod
    def bridge_drift_to_settled(drift_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_remediated = drift_posture.get("is_remediated", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_remediated and not is_settled:
            return {
                "status": "caution",
                "notes": "Drift cleaned up but not settled. No drift-safe claim.",
                "drift_proof_notes": "Evolving transfer rules have stale finality posture."
            }

        return {
            "status": "bridged",
            "notes": "Settlement-rule and SSI drift cleanup ready.",
            "drift_proof_notes": "Cleanup matched with valid settlement instructions."
        }
