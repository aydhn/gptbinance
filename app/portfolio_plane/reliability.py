class ReliabilityLinkage:
    @staticmethod
    def check_reliability_starvation(core_investment: float, resilience_investment: float) -> bool:
        # Caution if resilience is starved
        if core_investment > 0 and (resilience_investment / core_investment) < 0.1:
            return True
        return False
