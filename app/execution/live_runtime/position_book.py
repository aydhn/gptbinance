from app.execution.live_runtime.models import (
    LivePositionBook,
    LivePosition,
    LiveFillRecord,
)
from datetime import datetime


class LivePositionManager:
    def __init__(self):
        self.book = LivePositionBook()

    def process_fill(self, fill: LiveFillRecord) -> None:
        if fill.symbol not in self.book.positions:
            self.book.positions[fill.symbol] = LivePosition(symbol=fill.symbol)

        pos = self.book.positions[fill.symbol]
        fill_qty = fill.qty if fill.side.upper() == "BUY" else -fill.qty

        # Simple average entry price calculation
        new_qty = pos.qty + fill_qty

        if pos.qty > 0 and fill_qty > 0:
            # Increasing long
            pos.avg_entry_price = (
                (pos.qty * pos.avg_entry_price) + (fill.qty * fill.price)
            ) / new_qty
        elif pos.qty < 0 and fill_qty < 0:
            # Increasing short
            pos.avg_entry_price = (
                (abs(pos.qty) * pos.avg_entry_price) + (fill.qty * fill.price)
            ) / abs(new_qty)
        elif (pos.qty > 0 and fill_qty < 0) or (pos.qty < 0 and fill_qty > 0):
            # Reducing position
            if abs(fill_qty) <= abs(pos.qty):
                # Partial or full close
                pnl = (fill.price - pos.avg_entry_price) * abs(fill_qty)
                if pos.qty < 0:
                    pnl = -pnl
                pos.realized_pnl += pnl
                if new_qty == 0:
                    pos.avg_entry_price = 0.0
            else:
                # Flip
                pnl = (fill.price - pos.avg_entry_price) * abs(pos.qty)
                if pos.qty < 0:
                    pnl = -pnl
                pos.realized_pnl += pnl
                pos.avg_entry_price = fill.price

        elif pos.qty == 0:
            pos.avg_entry_price = fill.price

        pos.qty = new_qty

        # Deduct fee from realized pnl (assuming fee is in quote asset for simplicity here)
        if fill.fee_asset == fill.symbol.replace("USDT", ""):
            # Very rough approximation if fee in base asset
            pos.realized_pnl -= fill.fee * fill.price
        else:
            pos.realized_pnl -= fill.fee

        self.book.last_updated = datetime.utcnow()

    def get_book(self) -> LivePositionBook:
        return self.book
