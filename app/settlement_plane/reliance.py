from typing import Dict, Any


class RelianceLinkage:
    @staticmethod
    def bridge_reliance_to_settled(reliance_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_recovering = reliance_posture.get("is_recovering", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_recovering and not is_settled:
            return {
                "status": "caution",
                "notes": "Reliance recovery active but not settled. No reliance-safe claim.",
                "reliance_proof_notes": "Recovered value lacks matched/final transfer posture."
            }

        return {
            "status": "bridged",
            "notes": "Harm recovery settlement ready.",
            "reliance_proof_notes": "Recovery matched with valid settlement instructions."
        }
