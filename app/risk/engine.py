class RiskEngine:
    def get_risk_posture(self) -> dict:
        # Export pretrade allocation-specific risk summaries
        # Risk approves size envelope, not just signal
        return {"max_notional_per_symbol": 50000.0}
