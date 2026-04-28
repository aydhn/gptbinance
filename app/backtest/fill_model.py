from typing import Optional
import uuid
from app.backtest.models import (
    SimulatedOrderIntent,
    SimulatedFill,
    FillModelDecision,
    BacktestStepContext,
    ExecutionAssumption,
)
from app.backtest.costs import CostCalculator
from app.backtest.enums import OrderSide, FillAssumption


class FillModel:
    def __init__(self, assumption: ExecutionAssumption):
        self.assumption = assumption
        self.cost_calculator = CostCalculator(
            assumption.cost_config, assumption.slippage_config
        )

    def simulate_fill(
        self, intent: SimulatedOrderIntent, next_bar_context: BacktestStepContext
    ) -> SimulatedFill:
        """
        Simulate a fill using the NEXT bar's context (since the intent was generated on the current bar close).
        """
        fill_price = 0.0

        if self.assumption.fill_assumption == FillAssumption.NEXT_BAR_OPEN:
            fill_price = next_bar_context.bar_open
        elif self.assumption.fill_assumption == FillAssumption.SAME_BAR_CLOSE:
            fill_price = (
                next_bar_context.bar_close
            )  # Assuming next_bar is actually the current bar in this mode.
        elif self.assumption.fill_assumption == FillAssumption.WORST_CASE:
            fill_price = (
                next_bar_context.bar_high
                if intent.side == OrderSide.BUY
                else next_bar_context.bar_low
            )
        else:
            fill_price = next_bar_context.bar_open  # fallback

        # Apply slippage
        adjusted_price = self.cost_calculator.apply_slippage_to_price(
            fill_price, intent.side == OrderSide.BUY
        )

        # Apply fee
        notional_value = adjusted_price * intent.quantity
        fee = self.cost_calculator.calculate_cost(notional_value, is_maker=False)
        slippage_val = abs(adjusted_price - fill_price) * intent.quantity

        decision = FillModelDecision(
            accepted=True,
            fill_price=adjusted_price,
            fill_quantity=intent.quantity,
            fill_timestamp=next_bar_context.timestamp,
            fee_paid=fee,
            slippage_applied=slippage_val,
            reason="Simulated execution",
        )

        return SimulatedFill(
            fill_id=str(uuid.uuid4()),
            timestamp=next_bar_context.timestamp,
            intent=intent,
            decision=decision,
        )
