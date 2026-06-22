from typing import Dict, Any


class ImmunityLinkage:
    @staticmethod
    def bridge_immunity_to_settled(immunity_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_protected = immunity_posture.get("is_protected", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_protected and not is_settled:
            return {
                "status": "caution",
                "notes": "Protected transfer but not settled. No immunity-safe claim.",
                "immunity_proof_notes": "Protected payment has wrong account or reversal defect."
            }

        return {
            "status": "bridged",
            "notes": "Protected-beneficiary settlement posture secured.",
            "immunity_proof_notes": "Protected payment matched with valid settlement instructions."
        }
