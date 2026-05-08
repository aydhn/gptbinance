class RiskEngine:
    def get_risk_posture(self) -> dict:
        # Export pretrade allocation-specific risk summaries
        # Risk approves size envelope, not just signal
        return {"max_notional_per_symbol": 50000.0}

class RiskExecutionEnvelope:
    @staticmethod
    def get_envelope(symbol: str) -> dict:
        # Stub
        return {"max_aggressiveness": "passive", "max_clip_size": 100.0, "slippage_aware_clip_reason": None}
