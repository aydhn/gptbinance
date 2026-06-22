from typing import Dict, Any


class SuccessionLinkage:
    @staticmethod
    def bridge_succession_to_settled(succession_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_succeeded = succession_posture.get("is_succeeded", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_succeeded and not is_settled:
            return {
                "status": "caution",
                "notes": "Transfer succeeded but not settled. No succession-safe claim.",
                "succession_proof_notes": "Transferred obligations have broken SSI/beneficiary continuity."
            }

        return {
            "status": "bridged",
            "notes": "Successor transfer settlement ready.",
            "succession_proof_notes": "Successor transfer matched with valid settlement instructions."
        }
