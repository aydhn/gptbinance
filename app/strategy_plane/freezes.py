class StrategyFreezeGovernance:
    pass


class StrategyFreezeEvaluator:
    def evaluate_unfreeze(self, strategy_id: str, postmortem_debt: list) -> bool:
        if len(postmortem_debt) > 0:
            return False
        return True
