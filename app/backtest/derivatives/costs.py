import math
from typing import List
from .models import FundingEvent, BorrowCostEvent, DerivativeBacktestConfig

class BacktestCostSimulator:
    def __init__(self, config: DerivativeBacktestConfig):
        self.config = config
        self.funding_events: List[FundingEvent] = []
        self.borrow_events: List[BorrowCostEvent] = []

    def simulate_funding(self, timestamp: float, symbol: str, position_qty: float, mark_price: float):
        if position_qty == 0:
            return

        # Simplified: rate * notional. Long pays short if rate is positive
        notional = position_qty * mark_price
        cost = notional * self.config.hourly_funding_rate

        self.funding_events.append(FundingEvent(
            timestamp=timestamp,
            symbol=symbol,
            amount=-cost # Negative means paid
        ))

    def simulate_borrow(self, timestamp: float, asset: str, borrowed_amount: float):
        if borrowed_amount <= 0:
            return

        cost = borrowed_amount * self.config.hourly_borrow_rate
        self.borrow_events.append(BorrowCostEvent(
            timestamp=timestamp,
            asset=asset,
            amount=-cost
        ))
