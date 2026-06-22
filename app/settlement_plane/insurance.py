from typing import Dict, Any


class InsuranceLinkage:
    @staticmethod
    def bridge_insurance_to_settled(insurance_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_approved = insurance_posture.get("is_approved", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_approved and not is_settled:
            return {
                "status": "caution",
                "notes": "Insurance approved but payout not settled. No insurance-safe claim.",
                "insurance_proof_notes": "Approved payout lacks correct settlement and finality posture."
            }

        return {
            "status": "bridged",
            "notes": "Payout settlement ready.",
            "insurance_proof_notes": "Payout matched with valid settlement instructions."
        }
