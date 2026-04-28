import math
from typing import List
from app.backtest.validation.models import SampleSplitPlan, SampleWindow
from app.backtest.validation.enums import SampleSplitType


class SampleSplitter:
    """Generates simple IS/OOS split plans for future walk-forward context."""

    def create_simple_split(
        self,
        symbol: str,
        interval: str,
        start_ts: int,
        end_ts: int,
        is_ratio: float = 0.7,
    ) -> SampleSplitPlan:
        """Splits the full range into one IS and one OOS contiguous block."""
        total_duration = end_ts - start_ts
        split_point = start_ts + int(total_duration * is_ratio)

        windows = [
            SampleWindow(
                start_ts=start_ts,
                end_ts=split_point,
                split_type=SampleSplitType.IN_SAMPLE,
                description="Contiguous In-Sample",
            ),
            SampleWindow(
                start_ts=split_point,
                end_ts=end_ts,
                split_type=SampleSplitType.OUT_OF_SAMPLE,
                description="Contiguous Out-Of-Sample",
            ),
        ]

        return SampleSplitPlan(symbol=symbol, interval=interval, windows=windows)
