class QualityManager:
    def evaluate_quality(self, security_id: str) -> dict:
        return {
            "security_id": security_id,
            "phantom_collateral_warning": False,
            "duplicate_pledge_warning": False,
            "premature_release_warning": False,
            "stale_valuation_warning": False,
            "wrongful_draw_obstruction_warning": False,
            "under_security_warning": False,
            "quality_verdict": "high"
        }
