from typing import List, Optional
from app.strategies.models import EntryIntentCandidate, ExitIntentCandidate
from app.backtest.models import SimulatedOrderIntent, PositionState
from app.backtest.enums import OrderSide, PositionSide


class OrderIntentMapper:
    @staticmethod
    def from_entry_intent(
        intent: EntryIntentCandidate,
        position: PositionState,
        available_capital: float,
        current_price: float,
    ) -> Optional[SimulatedOrderIntent]:
        # Basic mapping logic.
        # In a real system, you'd calculate position sizing based on risk. Here we use a fixed simple size for now or full capital.
        if current_price <= 0:
            return None

        qty = (
            available_capital * 0.99
        ) / current_price  # Simple: use 99% of available capital
        if qty <= 0:
            return None

        return SimulatedOrderIntent(
            timestamp=intent.timestamp,
            symbol=intent.symbol,
            side=OrderSide.BUY if intent.direction.value == "long" else OrderSide.SELL,
            quantity=qty,
            is_reduce_only=False,
            intent_source=intent.strategy_name,
            rationale="Entry Intent",
        )

    @staticmethod
    def from_exit_intent(
        intent: ExitIntentCandidate, position: PositionState
    ) -> Optional[SimulatedOrderIntent]:
        if position.side == PositionSide.FLAT or position.quantity <= 0:
            return None

        return SimulatedOrderIntent(
            timestamp=intent.timestamp,
            symbol=intent.symbol,
            side=(
                OrderSide.SELL if position.side == PositionSide.LONG else OrderSide.BUY
            ),
            quantity=position.quantity,
            is_reduce_only=True,
            intent_source=intent.strategy_name,
            rationale="Exit Intent",
        )
