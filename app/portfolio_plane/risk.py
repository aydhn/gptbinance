class RiskLinkage:
    @staticmethod
    def evaluate_risk_burden(downside_impact: float, mitigation_factor: float) -> float:
        return downside_impact * (1.0 - mitigation_factor)
