from typing import Dict, Any


class IndemnityLinkage:
    @staticmethod
    def bridge_indemnity_to_settled(indemnity_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_promised = indemnity_posture.get("is_promised", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_promised and not is_settled:
            return {
                "status": "caution",
                "notes": "Indemnity promised but not settled. No indemnity-safe claim.",
                "indemnity_proof_notes": "Reimbursement promise lacks settled transfer posture."
            }

        return {
            "status": "bridged",
            "notes": "Reimbursement settlement ready.",
            "indemnity_proof_notes": "Reimbursement matched with valid settlement instructions."
        }
