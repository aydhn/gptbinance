from typing import Dict, Any


class ResilienceLinkage:
    @staticmethod
    def bridge_resilience_to_settled(resilience_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_resilient = resilience_posture.get("is_resilient", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_resilient and not is_settled:
            return {
                "status": "caution",
                "notes": "Reserve released but not settled. No resilience-safe claim.",
                "resilience_proof_notes": "Stressed settlement flow has hidden cutoff/funding fragility."
            }

        return {
            "status": "bridged",
            "notes": "Settlement resilience posture secured.",
            "resilience_proof_notes": "Reserve release matched with valid settlement instructions."
        }
