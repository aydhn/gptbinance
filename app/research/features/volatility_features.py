import pandas as pd
import numpy as np

from app.research.features.base import BaseFeatureCalculator
from app.research.features.registry import FeatureRegistry
from app.research.features.models import FeatureSpec
from app.research.features.enums import FeatureCategory
from app.research.features.exceptions import InvalidFeatureSpecError


@FeatureRegistry.register
class TrueRangeFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "true_range"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.VOLATILITY

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        return 2

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        prev_close = df["close"].shift(1)
        tr1 = df["high"] - df["low"]
        tr2 = (df["high"] - prev_close).abs()
        tr3 = (df["low"] - prev_close).abs()

        res = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        res.name = spec.name
        return res


@FeatureRegistry.register
class ATRFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "atr"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.VOLATILITY

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        if not spec.window:
            raise InvalidFeatureSpecError("atr requires a window configuration")
        return spec.window.window_size + 1

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        if not spec.window:
            raise InvalidFeatureSpecError("atr requires a window configuration")

        window_size = spec.window.window_size
        min_periods = spec.window.min_periods

        tr_calc = TrueRangeFeature()
        tr_spec = FeatureSpec(name="true_range", category=FeatureCategory.VOLATILITY)
        tr = tr_calc(df, tr_spec)

        # typically Wilder's smoothing is used for ATR, but simple EMA is standard fallback
        res = tr.ewm(
            alpha=1 / window_size, min_periods=min_periods, adjust=False
        ).mean()
        res.name = f"{spec.name}_{window_size}"
        return res


@FeatureRegistry.register
class RollingStdFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "rolling_std"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.VOLATILITY

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        if not spec.window:
            raise InvalidFeatureSpecError("rolling_std requires a window configuration")
        return spec.window.window_size

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        if not spec.window:
            raise InvalidFeatureSpecError("rolling_std requires a window configuration")
        source = spec.params.get("source", "close")
        window_size = spec.window.window_size
        min_periods = spec.window.min_periods

        res = df[source].rolling(window=window_size, min_periods=min_periods).std()
        res.name = f"{spec.name}_{window_size}"
        return res


@FeatureRegistry.register
class NormalizedATRFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "natr"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.VOLATILITY

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        if not spec.window:
            raise InvalidFeatureSpecError("natr requires a window configuration")
        return spec.window.window_size + 1

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        if not spec.window:
            raise InvalidFeatureSpecError("natr requires a window configuration")

        atr_calc = ATRFeature()
        atr = atr_calc(df, spec)

        res = (atr / df["close"]) * 100
        res.name = f"{spec.name}_{spec.window.window_size}"
        return res
