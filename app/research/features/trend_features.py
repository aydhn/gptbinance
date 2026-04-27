import pandas as pd
import numpy as np

from app.research.features.base import BaseFeatureCalculator
from app.research.features.registry import FeatureRegistry
from app.research.features.models import FeatureSpec
from app.research.features.enums import FeatureCategory
from app.research.features.exceptions import InvalidFeatureSpecError


@FeatureRegistry.register
class SMAFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "sma"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.TREND

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        if not spec.window:
            raise InvalidFeatureSpecError("sma requires a window configuration")
        return spec.window.window_size

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        if not spec.window:
            raise InvalidFeatureSpecError("sma requires a window configuration")
        source = spec.params.get("source", "close")
        window_size = spec.window.window_size
        min_periods = spec.window.min_periods

        res = df[source].rolling(window=window_size, min_periods=min_periods).mean()
        res.name = f"{spec.name}_{window_size}"
        return res


@FeatureRegistry.register
class EMAFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "ema"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.TREND

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        if not spec.window:
            raise InvalidFeatureSpecError("ema requires a window configuration")
        # EMA practically needs more history for stability, but we require at least window size
        return spec.window.window_size

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        if not spec.window:
            raise InvalidFeatureSpecError("ema requires a window configuration")
        source = spec.params.get("source", "close")
        window_size = spec.window.window_size
        min_periods = spec.window.min_periods

        res = (
            df[source]
            .ewm(span=window_size, min_periods=min_periods, adjust=False)
            .mean()
        )
        res.name = f"{spec.name}_{window_size}"
        return res


@FeatureRegistry.register
class PriceDistanceToMAFeature(BaseFeatureCalculator):
    """Normalized distance of price to a moving average."""

    @classmethod
    def get_name(cls) -> str:
        return "price_dist_ma"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.TREND

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        if not spec.window:
            raise InvalidFeatureSpecError(
                "price_dist_ma requires a window configuration"
            )
        return spec.window.window_size

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        if not spec.window:
            raise InvalidFeatureSpecError(
                "price_dist_ma requires a window configuration"
            )
        source = spec.params.get("source", "close")
        ma_type = spec.params.get("ma_type", "sma")
        window_size = spec.window.window_size
        min_periods = spec.window.min_periods

        if ma_type == "sma":
            ma = df[source].rolling(window=window_size, min_periods=min_periods).mean()
        elif ma_type == "ema":
            ma = (
                df[source]
                .ewm(span=window_size, min_periods=min_periods, adjust=False)
                .mean()
            )
        else:
            raise InvalidFeatureSpecError(f"Unsupported ma_type '{ma_type}'")

        res = (df[source] - ma) / ma
        res.name = f"{spec.name}_{ma_type}_{window_size}"
        return res
