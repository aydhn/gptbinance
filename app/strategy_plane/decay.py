from app.strategy_plane.models import StrategyDecayReport
from app.strategy_plane.enums import DecaySeverity


class StrategyDecayAnalyzer:
    def analyze(
        self, strategy_id: str, performance_history: dict
    ) -> StrategyDecayReport:
        return StrategyDecayReport(
            strategy_id=strategy_id,
            severity=DecaySeverity.NONE,
            performance_decay="0%",
            capture_decay="0%",
            execution_drag_increase="0%",
            notes="Stable",
        )
