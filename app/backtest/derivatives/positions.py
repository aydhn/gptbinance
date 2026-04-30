from typing import Dict
import logging

logger = logging.getLogger(__name__)

class BacktestDerivativePositionState:
    def __init__(self):
        self.positions: Dict[str, float] = {} # symbol -> net_quantity (positive for long, negative for short)
        self.entry_prices: Dict[str, float] = {}

    def apply_fill(self, symbol: str, is_buy: bool, quantity: float, price: float) -> float:
        """
        Applies fill and returns realized PNL.
        """
        signed_qty = quantity if is_buy else -quantity
        current_qty = self.positions.get(symbol, 0.0)
        current_entry = self.entry_prices.get(symbol, 0.0)

        realized_pnl = 0.0

        # Opening or adding to position
        if current_qty == 0 or (current_qty > 0 and is_buy) or (current_qty < 0 and not is_buy):
            new_qty = current_qty + signed_qty
            # VWAP entry
            new_entry = ((abs(current_qty) * current_entry) + (quantity * price)) / abs(new_qty)
            self.positions[symbol] = new_qty
            self.entry_prices[symbol] = new_entry
        else:
            # Reducing or flipping position
            if abs(signed_qty) <= abs(current_qty):
                # Pure reduction
                realized_pnl = abs(signed_qty) * (price - current_entry) * (1 if current_qty > 0 else -1)
                self.positions[symbol] = current_qty + signed_qty
            else:
                # Flip
                closing_qty = abs(current_qty)
                realized_pnl = closing_qty * (price - current_entry) * (1 if current_qty > 0 else -1)

                new_qty = current_qty + signed_qty
                self.positions[symbol] = new_qty
                self.entry_prices[symbol] = price # New entry is fill price

        if self.positions[symbol] == 0:
            self.entry_prices[symbol] = 0.0

        return realized_pnl
