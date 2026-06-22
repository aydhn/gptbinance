from typing import Dict, Any


class EffectuationLinkage:
    @staticmethod
    def bridge_effectuation_to_settled(effectuation_posture: Dict[str, Any], settlement_readiness: Dict[str, Any]) -> Dict[str, Any]:
        is_completed = effectuation_posture.get("is_completed", False)
        is_settled = settlement_readiness.get("overall_ready", False)

        if is_completed and not is_settled:
            return {
                "status": "caution",
                "notes": "Workflow completed but not settled. No effectuation-safe claim.",
                "effectuation_proof_notes": "Completed workflow lacks actual settled transfer."
            }

        return {
            "status": "bridged",
            "notes": "Workflow-to-settlement effectuation ready.",
            "effectuation_proof_notes": "Workflow matched with valid settlement instructions."
        }
