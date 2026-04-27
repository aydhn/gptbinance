import pandas as pd
import numpy as np

from app.research.features.base import BaseFeatureCalculator
from app.research.features.registry import FeatureRegistry
from app.research.features.models import FeatureSpec
from app.research.features.enums import FeatureCategory
from app.research.features.exceptions import InvalidFeatureSpecError


@FeatureRegistry.register
class PivotHighFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "pivot_high"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.STRUCTURE

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        left = spec.params.get("left", 2)
        right = spec.params.get("right", 2)
        return left + right + 1

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        left = spec.params.get("left", 2)
        right = spec.params.get("right", 2)

        # A pivot high exists at i if it's the strict maximum in window [i-left, i+right]
        # To avoid lookahead bias in real-time, this feature effectively identifies a pivot that occurred 'right' bars ago.
        # But for the sake of feature generation, we place the boolean AT the time it is CONFIRMED (i.e. at i + right).
        # OR we place it at the pivot, and accept it as a retrospective feature.
        # Research standard: features should not look ahead. If we want it aligned with 'now', the signal happens at `i + right`.
        # However, many times we want the *price* of the last confirmed pivot.

        # Let's create a rolling window to find max.
        window = left + right + 1
        rolling_max = df["high"].rolling(window=window).max()

        # The pivot occurred at i-right.
        # It is confirmed at i.
        # Is the value at i-right equal to the rolling max?
        pivot_val = df["high"].shift(right)
        is_pivot = (pivot_val == rolling_max) & (pivot_val.notna())

        res = is_pivot.astype(int)
        res.name = f"{spec.name}_{left}_{right}"
        return res


@FeatureRegistry.register
class PivotLowFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "pivot_low"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.STRUCTURE

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        left = spec.params.get("left", 2)
        right = spec.params.get("right", 2)
        return left + right + 1

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        left = spec.params.get("left", 2)
        right = spec.params.get("right", 2)

        window = left + right + 1
        rolling_min = df["low"].rolling(window=window).min()

        pivot_val = df["low"].shift(right)
        is_pivot = (pivot_val == rolling_min) & (pivot_val.notna())

        res = is_pivot.astype(int)
        res.name = f"{spec.name}_{left}_{right}"
        return res


@FeatureRegistry.register
class LastPivotHighPriceFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "last_pivot_high_price"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.STRUCTURE

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        left = spec.params.get("left", 2)
        right = spec.params.get("right", 2)
        return left + right + 1

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        left = spec.params.get("left", 2)
        right = spec.params.get("right", 2)

        ph_spec = FeatureSpec(
            name="pivot_high",
            category=FeatureCategory.STRUCTURE,
            params={"left": left, "right": right},
        )
        is_pivot = PivotHighFeature()(df, ph_spec)

        # When is_pivot is 1, the pivot price is high[i-right]
        pivot_prices = df["high"].shift(right).where(is_pivot == 1, np.nan)
        res = pivot_prices.ffill()

        res.name = f"{spec.name}_{left}_{right}"
        return res


@FeatureRegistry.register
class LastPivotLowPriceFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "last_pivot_low_price"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.STRUCTURE

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        left = spec.params.get("left", 2)
        right = spec.params.get("right", 2)
        return left + right + 1

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        left = spec.params.get("left", 2)
        right = spec.params.get("right", 2)

        pl_spec = FeatureSpec(
            name="pivot_low",
            category=FeatureCategory.STRUCTURE,
            params={"left": left, "right": right},
        )
        is_pivot = PivotLowFeature()(df, pl_spec)

        pivot_prices = df["low"].shift(right).where(is_pivot == 1, np.nan)
        res = pivot_prices.ffill()

        res.name = f"{spec.name}_{left}_{right}"
        return res
