from typing import Dict, Any


class AppealLinkage:
    @staticmethod
    def bridge_appeal_to_settled(appeal_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_reversed = appeal_posture.get("is_reversed", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_reversed and not is_settled:
            return {
                "status": "caution",
                "notes": "Payout reversed but not settled. No appeal-safe claim.",
                "appeal_proof_notes": "Reversed payout has stale reversal window or hidden duplicate exposure."
            }

        return {
            "status": "bridged",
            "notes": "Reversal-sensitive settlement ready.",
            "appeal_proof_notes": "Reversal matched with valid settlement instructions."
        }
