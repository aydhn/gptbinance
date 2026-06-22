from typing import Dict, Any


class NettingLinkage:
    @staticmethod
    def bridge_netting_to_settled(netting_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        """
        No netting-safe claim under legal zero narrative with no settled residual transfer posture.
        """
        is_netted = netting_posture.get("is_netted", False)
        residual_exposure = netting_posture.get("residual_exposure", 0)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_netted and residual_exposure > 0 and not is_settled:
            return {
                "status": "caution",
                "notes": "Netted with residual exposure, but not settled. No netting-safe claim.",
                "netting_proof_notes": "Legal zero narrative lacks settled residual transfer."
            }

        return {
            "status": "bridged",
            "notes": "Net exposure settlement ready.",
            "netting_proof_notes": "Residual exposure has valid settlement path."
        }
