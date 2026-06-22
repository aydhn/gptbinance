from typing import Dict, Any


class WarrantyLinkage:
    @staticmethod
    def bridge_warranty_to_settled(warranty_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_curing = warranty_posture.get("is_curing", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_curing and not is_settled:
            return {
                "status": "caution",
                "notes": "Warranty cure active but not settled. No warranty-safe claim.",
                "warranty_proof_notes": "Cure payment lacks final beneficiary settlement posture."
            }

        return {
            "status": "bridged",
            "notes": "Cure settlement ready.",
            "warranty_proof_notes": "Cure matched with valid settlement instructions."
        }
