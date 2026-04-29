"""Simulates fills for paper orders based on live data."""
import logging
from typing import List, Optional
from .models import PaperOrder, PaperFill, FillTrigger
import uuid

logger = logging.getLogger(__name__)


class PaperFillSimulator:
    def __init__(
        self,
        trigger: FillTrigger,
        max_slippage_pct: float,
        maker_fee_pct: float,
        taker_fee_pct: float,
    ):
        self.trigger = trigger
        self.max_slippage_pct = max_slippage_pct
        self.maker_fee_pct = maker_fee_pct
        self.taker_fee_pct = taker_fee_pct

    def evaluate(
        self, open_orders: List[PaperOrder], current_price: float, is_closed_bar: bool
    ) -> List[PaperFill]:
        """Evaluate open orders against current market data to generate fills."""
        fills = []
        for order in open_orders:
            if order.status not in ["created", "queued", "accepted"]:
                continue

            should_fill = False

            if self.trigger == FillTrigger.NEXT_TICK:
                should_fill = True
            elif self.trigger == FillTrigger.NEXT_BAR and is_closed_bar:
                should_fill = True
            elif self.trigger == FillTrigger.IMMEDIATE:
                should_fill = True

            if should_fill:
                # Simulate slippage (very basic: random or fixed penalty. Here we just apply worst case slippage penalty to keep it conservative)
                slippage = current_price * self.max_slippage_pct
                fill_price = (
                    current_price + slippage
                    if order.side.upper() == "BUY"
                    else current_price - slippage
                )

                # Assume taker fee for market-like fills
                notional = fill_price * order.qty
                fee = notional * self.taker_fee_pct

                fill = PaperFill(
                    fill_id=f"fill_{uuid.uuid4().hex[:8]}",
                    order_id=order.order_id,
                    symbol=order.symbol,
                    side=order.side,
                    qty=order.qty,
                    price=fill_price,
                    fees=fee,
                    slippage=slippage,
                )
                fills.append(fill)
        return fills
