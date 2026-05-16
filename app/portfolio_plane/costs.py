class CostLinkage:
    @staticmethod
    def validate_budget_envelope(requested: float, envelope: float) -> bool:
        return requested <= envelope
