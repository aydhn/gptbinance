from typing import Dict, Any


class StewardshipLinkage:
    @staticmethod
    def bridge_stewardship_to_settled(stewardship_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_restituted = stewardship_posture.get("is_restituted", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_restituted and not is_settled:
            return {
                "status": "caution",
                "notes": "Custodial flow restitiuted but not settled. No stewardship-safe claim.",
                "stewardship_proof_notes": "Preserved assets have broken custody/settlement chain."
            }

        return {
            "status": "bridged",
            "notes": "Custodial settlement integrity secured.",
            "stewardship_proof_notes": "Restitution matched with valid settlement instructions."
        }
