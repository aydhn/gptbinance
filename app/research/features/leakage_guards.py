import pandas as pd
from typing import List

from app.research.features.exceptions import LeakageError


class LeakageGuard:
    """
    Guards against potential data leakage (lookahead bias) during feature generation.
    """

    @staticmethod
    def check_future_leak(
        df: pd.DataFrame, feature_series: pd.Series, max_allowed_shift: int = 0
    ) -> bool:
        """
        A heuristic check to see if a feature perfectly predicts the *next* return.
        This doesn't prove leakage definitively, but it's a strong warning sign.
        However, computationally expensive for every feature.
        Instead, we can check basic things like index alignment.
        """
        if not df.index.equals(feature_series.index):
            raise LeakageError(
                "Feature index does not match input dataframe index. Possible leakage via unaligned merge."
            )
        return True

    @staticmethod
    def enforce_closed_candle_shift(series: pd.Series) -> pd.Series:
        """
        If a feature relies on the 'close' of a candle, and we want to use it
        as a signal for the *current* open, it must be shifted by 1.
        This guard simply shifts the series.
        """
        return series.shift(1)

    @staticmethod
    def validate_warmup(series: pd.Series, min_history: int) -> int:
        """
        Calculates how many initial rows are null.
        If it's significantly less than min_history, something might be leaking
        (e.g., using future data to backfill).
        Returns the number of nulls at the start.
        """
        if series.empty:
            return 0

        # Count consecutive initial nulls
        null_mask = series.isna()
        if not null_mask.iloc[0]:
            return 0

        first_valid_index = series.first_valid_index()
        if first_valid_index is None:
            return len(series)

        loc = series.index.get_loc(first_valid_index)
        return int(loc)
