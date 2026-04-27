import pytest
import pandas as pd
from app.research.features.mtf_alignment import MTFAligner


def test_strict_closed_alignment():
    # 15m base dataframe
    ltf_dates = pd.date_range("2023-01-01 10:00:00", periods=5, freq="15min")
    base_df = pd.DataFrame({"close": [1, 2, 3, 4, 5]}, index=ltf_dates)

    # 1h target feature (e.g., calculated on 09:00 and 10:00 candles)
    # The 09:00 candle closes at 09:59:59. Its value should be available starting at 10:00.
    # The 10:00 candle closes at 10:59:59. Its value should be available starting at 11:00.
    htf_dates = pd.DatetimeIndex(
        ["2023-01-01 09:00:00", "2023-01-01 10:00:00", "2023-01-01 11:00:00"]
    )
    target_series = pd.Series([100, 200, 300], index=htf_dates)

    aligned = MTFAligner.align_strict_closed(base_df, target_series)

    # At 10:00, 10:15, 10:30, 10:45 we should only see the value from the 09:00 candle (which is 100)
    assert aligned.loc["2023-01-01 10:00:00"] == 100
    assert aligned.loc["2023-01-01 10:45:00"] == 100

    # If we had an 11:00 row in base_df, it would be 200. Let's add it to verify.
    ltf_dates_extended = pd.date_range("2023-01-01 10:00:00", periods=6, freq="15min")
    base_df_extended = pd.DataFrame(
        {"close": [1, 2, 3, 4, 5, 6]}, index=ltf_dates_extended
    )
    aligned_extended = MTFAligner.align_strict_closed(base_df_extended, target_series)

    assert aligned_extended.loc["2023-01-01 11:00:00"] == 200
