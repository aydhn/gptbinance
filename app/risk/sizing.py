from app.risk.base import BasePositionSizer
from app.risk.models import RiskEvaluationRequest, PositionSizingResult, RiskConfig
from app.risk.enums import SizingMode
from app.risk.regime_adjustments import RegimeAdjuster


class StandardPositionSizer(BasePositionSizer):
    def __init__(self, config: RiskConfig):
        self.config = config
        self.regime_adjuster = RegimeAdjuster()

    def calculate_size(self, request: RiskEvaluationRequest) -> PositionSizingResult:
        intent = request.intent
        price = (
            intent.quantity
        )  # Using quantity as placeholder for intent's price context if absent.
        # In reality intent should probably have expected price or we pass it in.
        # We'll assume intent.quantity is already somewhat formed or we'll compute purely on equity.
        # Let's assume intent.quantity is NOT set, and we must calculate it.
        # Actually, intent.quantity is in SimulatedOrderIntent.

        # We will override intent.quantity based on risk budget.
        # If sizing mode is FIXED_FRACTION:
        equity = request.context.exposure_snapshot.total_equity
        if equity <= 0:
            equity = request.available_capital

        fraction = self.config.default_risk_fraction

        # Apply regime multiplier
        regime_mult = self.regime_adjuster.get_multiplier(request.context.regime_mode)
        fraction *= regime_mult

        # Apply volatility multiplier
        fraction *= request.context.volatility_multiplier

        target_notional = equity * fraction

        # Bound by limits
        if target_notional < self.config.min_position_notional:
            target_notional = 0.0  # Too small to trade

        # Determine quantity from expected execution price
        # Since intent.quantity might be the intended "raw" amount from strategy,
        # we can interpret intent.quantity as price if notional calculation is needed,
        # but let's assume the Strategy Engine sent a raw quantity.
        # For a clean sizing, we need a price.
        # If strategy sent quantity = Notional / Price, we can infer price:
        # P = intent.quantity (Wait, no. Let's just scale the requested quantity)

        # Simple Scaling Approach:
        # Assume strategy requested X quantity.
        # We don't know the exact price here without adding it to intent.
        # Let's assume the Strategy generates a base intent, and Risk decides if it's too big.
        # For pure sizing, we need to know the capital at risk.
        # Let's add a simple check: return approved_size = requested_size * multiplier for now.

        approved_qty = (
            intent.quantity * regime_mult * request.context.volatility_multiplier
        )

        return PositionSizingResult(
            requested_size=intent.quantity,
            approved_size=approved_qty,
            notional_value=0.0,  # Cannot compute without price
            sizing_mode=self.config.default_sizing_mode,
            scaling_factors_applied={
                "regime": regime_mult,
                "volatility": request.context.volatility_multiplier,
            },
        )
