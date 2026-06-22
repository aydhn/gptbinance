from typing import Dict, Any


class RenewalLinkage:
    @staticmethod
    def bridge_renewal_to_settled(renewal_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_continuing = renewal_posture.get("is_continuing", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_continuing and not is_settled:
            return {
                "status": "caution",
                "notes": "Instruction continuing but not settled. No renewal-safe claim.",
                "renewal_proof_notes": "Rolled-forward transfer flows have stale SSI or stale cut-off assumptions."
            }

        return {
            "status": "bridged",
            "notes": "Continuing instruction settlement ready.",
            "renewal_proof_notes": "Continuation matched with valid settlement instructions."
        }
