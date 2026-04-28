from typing import Generator, Dict, Any, List
from datetime import datetime, timedelta
from app.backtest.models import BacktestStepContext
import random


class ReplayDriver:
    """
    Mock Replay Driver for Phase 09.
    In a real scenario, this reads from local parquet/csv files.
    """

    def __init__(
        self, symbol: str, interval: str, start_time: datetime, end_time: datetime
    ):
        self.symbol = symbol
        self.interval = interval
        self.start_time = start_time
        self.end_time = end_time

        # Simple interval parser for mock
        self.delta = timedelta(minutes=15)
        if interval == "1h":
            self.delta = timedelta(hours=1)
        elif interval == "1d":
            self.delta = timedelta(days=1)

    def generate_steps(self) -> Generator[BacktestStepContext, None, None]:
        current = self.start_time
        price = 100.0  # starting price

        while current <= self.end_time:
            # Random walk
            change = random.uniform(-0.02, 0.02)
            open_p = price
            close_p = price * (1 + change)
            high_p = max(open_p, close_p) * (1 + random.uniform(0, 0.01))
            low_p = min(open_p, close_p) * (1 - random.uniform(0, 0.01))

            # Mock features
            features = {
                "close": close_p,
                "high": high_p,
                "low": low_p,
                "trend_sma_fast": close_p * 0.99,
                "trend_sma_slow": close_p * 0.95,
                "volatility_atr": close_p * 0.05,
            }

            yield BacktestStepContext(
                timestamp=current,
                bar_open=open_p,
                bar_high=high_p,
                bar_low=low_p,
                bar_close=close_p,
                bar_volume=random.uniform(10, 100),
                features=features,
            )

            price = close_p
            current += self.delta
