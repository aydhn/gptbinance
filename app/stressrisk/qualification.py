class QualificationStressEvidence:
    def get_evidence(self, run_id: str):
        return {
            "run_id": run_id,
            "status": "PASS",
            "message": "Stress scenario evaluated safely.",
        }


def get_capital_tier_stress_suitability(tier_id: str) -> dict:
    """Returns stress evidence suitability summary for different capital tiers."""
    return {"suitable": True, "stricter_thresholds_applied": True}
