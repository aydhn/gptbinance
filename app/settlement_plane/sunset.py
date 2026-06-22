from typing import Dict, Any


class SunsetLinkage:
    @staticmethod
    def bridge_sunset_to_settled(sunset_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_tail = sunset_posture.get("is_tail", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_tail and not is_settled:
            return {
                "status": "caution",
                "notes": "Tail payout but not settled. No sunset-safe claim.",
                "sunset_proof_notes": "Retired-state tail payment has hidden fail residue."
            }

        return {
            "status": "bridged",
            "notes": "Tail settlement posture ready.",
            "sunset_proof_notes": "Tail payout matched with valid settlement instructions."
        }
