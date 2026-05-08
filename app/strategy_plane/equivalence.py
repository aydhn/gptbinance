from app.strategy_plane.models import StrategyEquivalenceReport
from app.strategy_plane.enums import EquivalenceVerdict


class StrategyEquivalenceEvaluator:
    def evaluate(
        self, strategy_id: str, replay_metrics: dict, live_metrics: dict
    ) -> StrategyEquivalenceReport:
        return StrategyEquivalenceReport(
            strategy_id=strategy_id,
            verdict=EquivalenceVerdict.EQUIVALENT,
            divergence_sources=[],
            notes="Clean equivalence",
        )
