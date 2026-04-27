import pandas as pd
from app.research.features.exceptions import AlignmentError


class MTFAligner:
    """
    Handles Multi-Timeframe (MTF) Alignment.
    """

    @staticmethod
    def align_strict_closed(
        base_df: pd.DataFrame, target_series: pd.Series
    ) -> pd.Series:
        """
        Aligns a feature calculated on a higher timeframe (target_series)
        onto a lower timeframe (base_df).

        STRICT CLOSED rule:
        A 1H feature value is only available to the 15m candles that open *after* the 1H candle closes.
        E.g., 10:00-11:00 1H candle closes at 10:59:59.
        Its feature value is only valid for the 11:00 15m candle onwards.

        Both base_df and target_series must have DateTimeIndex.
        """
        if not isinstance(base_df.index, pd.DatetimeIndex):
            raise AlignmentError("base_df must have a DatetimeIndex for MTF alignment.")
        if not isinstance(target_series.index, pd.DatetimeIndex):
            raise AlignmentError(
                "target_series must have a DatetimeIndex for MTF alignment."
            )

        # target_series index represents the OPEN time of the HTF candle.
        # However, many times people shift it so the index is the CLOSE time.
        # Assuming the index is the OPEN time of the candle (standard in crypto).
        # We must shift the target_series by 1 HTF period before forward filling,
        # otherwise we leak the HTF close into the LTF candles that make up that HTF candle.

        # 1. Shift the HTF series by 1
        shifted_target = target_series.shift(1)

        # 2. Reindex to the LTF index, using forward fill
        # This means at 10:15, it looks for the last value before or at 10:15 in the shifted target.
        # Since 10:00 was shifted to 11:00, at 10:15 it will see the value from 09:00 (which was shifted to 10:00).
        # This is exactly what we want.
        aligned = shifted_target.reindex(base_df.index, method="ffill")

        return aligned
