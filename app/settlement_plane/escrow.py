from typing import Dict, Any


class EscrowLinkage:
    @staticmethod
    def bridge_escrow_to_settled(escrow_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        """
        No escrow-safe claim under released escrow value with no final settlement discipline.
        """
        is_released = escrow_posture.get("is_released", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_released and not is_settled:
            return {
                "status": "caution",
                "notes": "Escrow released but not settled. No escrow-safe claim.",
                "escrow_proof_notes": "Released value lacks final settlement discipline."
            }

        return {
            "status": "bridged",
            "notes": "Held-value settlement release ready.",
            "escrow_proof_notes": "Release matched with valid settlement instructions."
        }
