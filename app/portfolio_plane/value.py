class ValueLinkage:
    @staticmethod
    def evaluate_value_density(expected_value: float, cost_estimate: float) -> float:
        if cost_estimate <= 0:
            return 0.0
        return expected_value / cost_estimate
