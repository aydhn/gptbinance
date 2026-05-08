from app.strategy_plane.models import StrategyOverlapReport


class StrategyOverlapDetector:
    def detect_overlap(
        self, strategy_id: str, active_strategies: list
    ) -> StrategyOverlapReport:
        return StrategyOverlapReport(
            strategy_id=strategy_id,
            overlapping_strategies=[],
            severity="NONE",
            notes="No overlap detected",
        )
