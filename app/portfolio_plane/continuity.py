class ContinuityLinkage:
    @staticmethod
    def check_continuity_debt(continuity_budget: float, total_budget: float) -> bool:
        if total_budget > 0 and (continuity_budget / total_budget) < 0.05:
            return True
        return False
