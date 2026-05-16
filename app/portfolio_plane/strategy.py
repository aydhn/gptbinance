class StrategyLinkage:
    @staticmethod
    def check_strategy_coherence(initiative_theme: str, active_strategies: list) -> bool:
        return initiative_theme in active_strategies
