from app.strategy_plane.models import StrategyFitReport
from app.strategy_plane.enums import FitClass


class StrategyFitEvaluator:
    def evaluate_fit(
        self, strategy_id: str, regime_context: str, execution_context: str
    ) -> StrategyFitReport:
        # Dummy logic for structural placeholder
        return StrategyFitReport(
            strategy_id=strategy_id,
            regime_fit=FitClass.STRONG_FIT,
            sleeve_fit=FitClass.STRONG_FIT,
            liquidity_fit=FitClass.STRONG_FIT,
            risk_fit=FitClass.STRONG_FIT,
            notes="Evaluated via static rules",
        )
