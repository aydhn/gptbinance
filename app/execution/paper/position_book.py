"""Paper position book management."""
from typing import Dict, List
from .models import PaperPosition, PaperFill


class PositionBookManager:
    def __init__(self):
        self.positions: Dict[str, PaperPosition] = {}

    def get_position(self, symbol: str) -> PaperPosition:
        if symbol not in self.positions:
            self.positions[symbol] = PaperPosition(symbol=symbol)
        return self.positions[symbol]

    def process_fill(self, fill: PaperFill) -> float:
        """Update position based on fill and return realized PnL from this fill."""
        pos = self.get_position(fill.symbol)
        realized_pnl = 0.0

        fill_qty = fill.qty if fill.side.upper() == "BUY" else -fill.qty

        # If flat, just open
        if pos.qty == 0:
            pos.qty = fill_qty
            pos.avg_entry_price = fill.price
            pos.side = "LONG" if fill_qty > 0 else "SHORT"
            return realized_pnl

        # Same direction (scaling in)
        if (pos.qty > 0 and fill_qty > 0) or (pos.qty < 0 and fill_qty < 0):
            total_qty = pos.qty + fill_qty
            total_cost = (pos.qty * pos.avg_entry_price) + (fill_qty * fill.price)
            pos.avg_entry_price = total_cost / total_qty
            pos.qty = total_qty
        # Opposite direction (scaling out or reversing)
        else:
            if abs(fill_qty) <= abs(pos.qty):
                # Pure scale out
                if pos.qty > 0:  # Long
                    realized_pnl = abs(fill_qty) * (fill.price - pos.avg_entry_price)
                else:  # Short
                    realized_pnl = abs(fill_qty) * (pos.avg_entry_price - fill.price)

                pos.qty += fill_qty
                if pos.qty == 0:
                    pos.side = "FLAT"
                    pos.avg_entry_price = 0.0
            else:
                # Reverse
                # 1. Close existing
                close_qty = abs(pos.qty)
                if pos.qty > 0:
                    realized_pnl = close_qty * (fill.price - pos.avg_entry_price)
                else:
                    realized_pnl = close_qty * (pos.avg_entry_price - fill.price)

                # 2. Open new
                pos.qty += fill_qty
                pos.avg_entry_price = fill.price
                pos.side = "LONG" if pos.qty > 0 else "SHORT"

        pos.realized_pnl += realized_pnl
        return realized_pnl

    def get_all(self) -> List[PaperPosition]:
        return list(self.positions.values())
