from typing import Dict, Any


class ClearingLinkage:
    @staticmethod
    def bridge_cleared_to_settled(clearing_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        """
        No clearing-safe claim under novated trade with no final settlement posture where claimed.
        """
        is_cleared = clearing_posture.get("is_cleared", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_cleared and not is_settled:
            return {
                "status": "caution",
                "notes": "Cleared but not settled. No clearing-safe claim under novated trade with no final settlement posture.",
                "clearing_proof_notes": "Novated trade lacks settlement confirmation."
            }

        return {
            "status": "bridged",
            "notes": "Cleared and settlement-ready.",
            "clearing_proof_notes": "Novation matched with valid settlement instructions."
        }
