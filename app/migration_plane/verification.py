from typing import Dict, Any

class MigrationVerification:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("migration_acceptance_masking"):
            return {"status": "caution", "reason": "migration_complete_claim_under_adversarial_narrative_gap"}
        return {"status": "ok"}
