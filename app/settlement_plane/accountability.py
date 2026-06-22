from typing import Dict, Any


class AccountabilityLinkage:
    @staticmethod
    def bridge_accountability_to_settled(accountability_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_sanctioned = accountability_posture.get("is_sanctioned", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_sanctioned and not is_settled:
            return {
                "status": "caution",
                "notes": "Sanction ordered but not settled. No accountability-safe claim.",
                "accountability_proof_notes": "Corrected transfer flow has hidden beneficiary harm tail."
            }

        return {
            "status": "bridged",
            "notes": "Sanction/remediation settlement posture ready.",
            "accountability_proof_notes": "Sanction collection matched with valid settlement instructions."
        }
