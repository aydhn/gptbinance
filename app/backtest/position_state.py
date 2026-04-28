from datetime import datetime
from typing import Optional, Tuple
from app.backtest.models import PositionState, SimulatedFill
from app.backtest.enums import PositionSide, OrderSide
from app.backtest.exceptions import PositionStateError


class PositionManager:
    def __init__(self, symbol: str):
        self.state = PositionState(symbol=symbol)

    def apply_fill(self, fill: SimulatedFill) -> Tuple[PositionState, float]:
        """
        Applies a simulated fill to the position state.
        Returns the updated state and the realized PnL from this fill (if any).
        """
        decision = fill.decision
        if not decision.accepted:
            return self.state, 0.0

        is_buy = fill.intent.side == OrderSide.BUY
        fill_qty = decision.fill_quantity
        fill_price = decision.fill_price

        realized_pnl = 0.0

        # Determine fill side effect
        if self.state.side == PositionSide.FLAT:
            # Opening new position
            self.state.side = PositionSide.LONG if is_buy else PositionSide.SHORT
            self.state.quantity = fill_qty
            self.state.entry_price = fill_price
            self.state.open_timestamp = decision.fill_timestamp
        elif self.state.side == PositionSide.LONG:
            if is_buy:
                # Adding to long (average price calculation)
                total_cost = (self.state.quantity * self.state.entry_price) + (
                    fill_qty * fill_price
                )
                self.state.quantity += fill_qty
                self.state.entry_price = total_cost / self.state.quantity
            else:
                # Reducing or closing long
                close_qty = min(self.state.quantity, fill_qty)
                realized_pnl = (fill_price - self.state.entry_price) * close_qty
                self.state.realized_pnl += realized_pnl

                self.state.quantity -= close_qty

                if self.state.quantity <= 1e-8:  # floating point protection
                    self.state.side = PositionSide.FLAT
                    self.state.quantity = 0.0
                    self.state.entry_price = 0.0

                # Handle reverse
                remaining_qty = fill_qty - close_qty
                if remaining_qty > 1e-8:
                    self.state.side = PositionSide.SHORT
                    self.state.quantity = remaining_qty
                    self.state.entry_price = fill_price
                    self.state.open_timestamp = decision.fill_timestamp

        elif self.state.side == PositionSide.SHORT:
            if not is_buy:
                # Adding to short
                total_cost = (self.state.quantity * self.state.entry_price) + (
                    fill_qty * fill_price
                )
                self.state.quantity += fill_qty
                self.state.entry_price = total_cost / self.state.quantity
            else:
                # Reducing or closing short
                close_qty = min(self.state.quantity, fill_qty)
                realized_pnl = (
                    self.state.entry_price - fill_price
                ) * close_qty  # Short PnL
                self.state.realized_pnl += realized_pnl

                self.state.quantity -= close_qty

                if self.state.quantity <= 1e-8:
                    self.state.side = PositionSide.FLAT
                    self.state.quantity = 0.0
                    self.state.entry_price = 0.0

                # Handle reverse
                remaining_qty = fill_qty - close_qty
                if remaining_qty > 1e-8:
                    self.state.side = PositionSide.LONG
                    self.state.quantity = remaining_qty
                    self.state.entry_price = fill_price
                    self.state.open_timestamp = decision.fill_timestamp

        self.state.last_update_timestamp = decision.fill_timestamp

        # Set the realized pnl on the fill object for the ledger
        fill.realized_pnl = realized_pnl

        return self.state, realized_pnl

    def update_unrealized_pnl(self, current_price: float):
        if self.state.side == PositionSide.FLAT:
            self.state.unrealized_pnl = 0.0
        elif self.state.side == PositionSide.LONG:
            self.state.unrealized_pnl = (
                current_price - self.state.entry_price
            ) * self.state.quantity
        elif self.state.side == PositionSide.SHORT:
            self.state.unrealized_pnl = (
                self.state.entry_price - current_price
            ) * self.state.quantity
