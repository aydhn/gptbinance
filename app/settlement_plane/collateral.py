from typing import Dict, Any


class CollateralLinkage:
    @staticmethod
    def bridge_collateral_to_settled(collateral_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        """
        No collateral-safe claim under realized value with no correct delivery/payment finality.
        """
        is_liquidated = collateral_posture.get("is_liquidated", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_liquidated and not is_settled:
            return {
                "status": "caution",
                "notes": "Collateral liquidated but not settled. No collateral-safe claim.",
                "collateral_proof_notes": "Realized value lacks correct delivery/payment finality."
            }

        return {
            "status": "bridged",
            "notes": "Liquidation settlement ready.",
            "collateral_proof_notes": "Liquidation matched with valid settlement instructions."
        }
