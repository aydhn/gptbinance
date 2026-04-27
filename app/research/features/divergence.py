import pandas as pd
import numpy as np

from app.research.features.base import BaseFeatureCalculator
from app.research.features.registry import FeatureRegistry
from app.research.features.models import FeatureSpec
from app.research.features.enums import FeatureCategory, DivergenceType
from app.research.features.exceptions import InvalidFeatureSpecError
from app.research.features.structure_features import PivotHighFeature, PivotLowFeature


@FeatureRegistry.register
class BullishDivergenceCandidateFeature(BaseFeatureCalculator):
    """
    Identifies candidates for bullish divergence (Regular or Hidden).
    Returns an integer categorical:
    0 = None
    1 = Regular Bullish (Price LL, Osc HL)
    2 = Hidden Bullish (Price HL, Osc LL)
    """

    @classmethod
    def get_name(cls) -> str:
        return "bullish_divergence_candidate"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.DIVERGENCE

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        return 10  # Need enough history for at least two pivots

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        osc_column = spec.params.get("osc_column")
        if not osc_column or osc_column not in df.columns:
            # In a real pipeline, the osc column must be generated first and present in df
            # Or we raise an error. For flexibility, if it's not there, we return 0s
            return pd.Series(0, index=df.index, name=spec.name)

        left = spec.params.get("left", 2)
        right = spec.params.get("right", 2)

        # 1. Find Price Pivot Lows
        pl_spec = FeatureSpec(
            name="pivot_low",
            category=FeatureCategory.STRUCTURE,
            params={"left": left, "right": right},
        )
        is_pivot = PivotLowFeature()(df, pl_spec)

        # Create a dataframe to track pivot states
        # The pivot actually occurred at index - right.
        pivots = pd.DataFrame(index=df.index)
        pivots["is_pivot"] = is_pivot
        pivots["price"] = df["low"].shift(right)
        pivots["osc"] = df[osc_column].shift(right)

        # Forward fill the last known pivot values
        pivots["last_price"] = pivots["price"].where(pivots["is_pivot"] == 1).ffill()
        pivots["last_osc"] = pivots["osc"].where(pivots["is_pivot"] == 1).ffill()

        # Shift to get the previous pivot
        # We need the values of the pivot *before* the last one
        pivots["prev_price"] = pivots["last_price"].shift(1)
        # However, shifting by 1 shifts the ffilled column. We only want to compare when a NEW pivot is confirmed.

        # Better logic: extract only pivot rows, compute relations, then merge back
        pivot_rows = pivots[pivots["is_pivot"] == 1].copy()
        pivot_rows["prev_price"] = pivot_rows["price"].shift(1)
        pivot_rows["prev_osc"] = pivot_rows["osc"].shift(1)

        # Regular Bullish: Price LL, Osc HL
        pivot_rows["regular_bull"] = (
            pivot_rows["price"] < pivot_rows["prev_price"]
        ) & (pivot_rows["osc"] > pivot_rows["prev_osc"])

        # Hidden Bullish: Price HL, Osc LL
        pivot_rows["hidden_bull"] = (pivot_rows["price"] > pivot_rows["prev_price"]) & (
            pivot_rows["osc"] < pivot_rows["prev_osc"]
        )

        pivot_rows["div_type"] = 0
        pivot_rows.loc[pivot_rows["regular_bull"], "div_type"] = 1
        pivot_rows.loc[pivot_rows["hidden_bull"], "div_type"] = 2

        # Merge back
        res = pd.Series(0, index=df.index)
        res.update(pivot_rows["div_type"])

        res.name = f"{spec.name}_{left}_{right}"
        return res


@FeatureRegistry.register
class BearishDivergenceCandidateFeature(BaseFeatureCalculator):
    """
    Identifies candidates for bearish divergence (Regular or Hidden).
    0 = None
    1 = Regular Bearish (Price HH, Osc LH)
    2 = Hidden Bearish (Price LH, Osc HH)
    """

    @classmethod
    def get_name(cls) -> str:
        return "bearish_divergence_candidate"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.DIVERGENCE

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        return 10

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        osc_column = spec.params.get("osc_column")
        if not osc_column or osc_column not in df.columns:
            return pd.Series(0, index=df.index, name=spec.name)

        left = spec.params.get("left", 2)
        right = spec.params.get("right", 2)

        ph_spec = FeatureSpec(
            name="pivot_high",
            category=FeatureCategory.STRUCTURE,
            params={"left": left, "right": right},
        )
        is_pivot = PivotHighFeature()(df, ph_spec)

        pivots = pd.DataFrame(index=df.index)
        pivots["is_pivot"] = is_pivot
        pivots["price"] = df["high"].shift(right)
        pivots["osc"] = df[osc_column].shift(right)

        pivot_rows = pivots[pivots["is_pivot"] == 1].copy()
        pivot_rows["prev_price"] = pivot_rows["price"].shift(1)
        pivot_rows["prev_osc"] = pivot_rows["osc"].shift(1)

        # Regular Bearish: Price HH, Osc LH
        pivot_rows["regular_bear"] = (
            pivot_rows["price"] > pivot_rows["prev_price"]
        ) & (pivot_rows["osc"] < pivot_rows["prev_osc"])

        # Hidden Bearish: Price LH, Osc HH
        pivot_rows["hidden_bear"] = (pivot_rows["price"] < pivot_rows["prev_price"]) & (
            pivot_rows["osc"] > pivot_rows["prev_osc"]
        )

        pivot_rows["div_type"] = 0
        pivot_rows.loc[pivot_rows["regular_bear"], "div_type"] = 1
        pivot_rows.loc[pivot_rows["hidden_bear"], "div_type"] = 2

        res = pd.Series(0, index=df.index)
        res.update(pivot_rows["div_type"])

        res.name = f"{spec.name}_{left}_{right}"
        return res
