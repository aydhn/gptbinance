from typing import Dict, Any


class OversightLinkage:
    @staticmethod
    def bridge_oversight_to_settled(oversight_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_monitored = oversight_posture.get("is_monitored", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_monitored and not is_settled:
            return {
                "status": "caution",
                "notes": "Flow monitored but not settled. No oversight-safe claim.",
                "oversight_proof_notes": "Monitored flow lacks fail/finality sufficiency."
            }

        return {
            "status": "bridged",
            "notes": "Supervised settlement posture ready.",
            "oversight_proof_notes": "Supervision matched with valid settlement instructions."
        }
