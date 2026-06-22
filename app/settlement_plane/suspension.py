from typing import Dict, Any


class SuspensionLinkage:
    @staticmethod
    def bridge_suspension_to_settled(suspension_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_suspended = suspension_posture.get("is_suspended", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_suspended and not is_settled:
            return {
                "status": "caution",
                "notes": "Flow suspended but provisional transfers exist. No suspension-safe claim.",
                "suspension_proof_notes": "Suspended flow has silent provisional transfer or fail carry."
            }

        return {
            "status": "bridged",
            "notes": "Frozen settlement posture secured.",
            "suspension_proof_notes": "Suspension matched with valid settlement instructions."
        }
