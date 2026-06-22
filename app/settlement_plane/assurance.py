from typing import Dict, Any


class AssuranceLinkage:
    @staticmethod
    def bridge_assurance_to_settled(assurance_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_assured = assurance_posture.get("is_assured", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_assured and not is_settled:
            return {
                "status": "caution",
                "notes": "Evidence backed but not settled. No assurance-safe claim.",
                "assurance_proof_notes": "Settled narrative has weak SSI, weak match or weak finality evidence."
            }

        return {
            "status": "bridged",
            "notes": "Evidence-backed settlement posture secured.",
            "assurance_proof_notes": "Correction matched with valid settlement instructions."
        }
