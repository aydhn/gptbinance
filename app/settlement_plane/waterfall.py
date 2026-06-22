from typing import Dict, Any


class WaterfallLinkage:
    @staticmethod
    def bridge_waterfall_to_settled(waterfall_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        """
        No waterfall-safe claim under allocated proceeds with no final beneficiary transfer posture.
        """
        is_allocated = waterfall_posture.get("is_allocated", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_allocated and not is_settled:
            return {
                "status": "caution",
                "notes": "Waterfall allocated but not settled. No waterfall-safe claim.",
                "waterfall_proof_notes": "Allocated proceeds lack final beneficiary transfer posture."
            }

        return {
            "status": "bridged",
            "notes": "Distribution settlement ready.",
            "waterfall_proof_notes": "Distribution matched with valid settlement instructions."
        }
