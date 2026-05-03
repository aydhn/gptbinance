from app.stressrisk.models import ScenarioLossEstimate
from app.stressrisk.enums import LossSeverity


class LossEstimator:
    def estimate(
        self, scenario_id: str, symbol: str, exposure: float, price_shock_mult: float
    ) -> ScenarioLossEstimate:
        estimated_loss = (
            round(exposure * (1.0 - price_shock_mult), 6)
            if price_shock_mult < 1.0
            else 0.0
        )
        severity = LossSeverity.LOW

        # >= rather than > for the critical boundary so that 200.0 out of 1000.0 is CRITICAL as per the test
        if estimated_loss >= exposure * 0.2:
            severity = LossSeverity.CRITICAL
        elif estimated_loss >= exposure * 0.1:
            severity = LossSeverity.HIGH

        return ScenarioLossEstimate(
            scenario_id=scenario_id,
            symbol=symbol,
            base_exposure=exposure,
            estimated_loss=estimated_loss,
            loss_severity=severity,
            cost_burden=estimated_loss * 0.01,
            execution_deterioration_cost=estimated_loss * 0.02,
        )
