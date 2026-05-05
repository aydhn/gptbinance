class ExperimentPolicyIntegration:
    def check_legality(self, candidate_diff: dict) -> bool:
        # Prevent touching forbidden surfaces like live trading flags
        if "live_trading_enabled" in candidate_diff:
            return False
        return True
