from typing import Dict, Any

class ChangeLinkage:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "emergency_shortcut_abuse": context.get("emergency_shortcut_abuse", "unknown"),
            "verification_theater": context.get("verification_theater", "unknown"),
            "rollback_narrative_abuse": context.get("rollback_narrative_abuse", "unknown"),
            "change_proof_notes": "No change-safe claim without exploit resistance",
            "collision_notes": []
        }
