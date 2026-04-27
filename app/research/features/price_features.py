import pandas as pd
import numpy as np

from app.research.features.base import BaseFeatureCalculator
from app.research.features.registry import FeatureRegistry
from app.research.features.models import FeatureSpec
from app.research.features.enums import FeatureCategory


@FeatureRegistry.register
class ReturnFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "return"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.PRICE

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        periods = spec.params.get("periods", 1)
        return periods + 1

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        periods = spec.params.get("periods", 1)
        res = df["close"].pct_change(periods=periods)
        res.name = f"{spec.name}_{periods}"
        return res


@FeatureRegistry.register
class LogReturnFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "log_return"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.PRICE

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        periods = spec.params.get("periods", 1)
        return periods + 1

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        periods = spec.params.get("periods", 1)
        res = np.log(df["close"] / df["close"].shift(periods))
        res.name = f"{spec.name}_{periods}"
        return res


@FeatureRegistry.register
class CandleBodyFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "candle_body"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.PRICE

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        return 1

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        res = df["close"] - df["open"]
        res.name = spec.name
        return res


@FeatureRegistry.register
class CandleRangeFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "candle_range"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.PRICE

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        return 1

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        res = df["high"] - df["low"]
        res.name = spec.name
        return res


@FeatureRegistry.register
class UpperWickFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "upper_wick"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.PRICE

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        return 1

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        res = df["high"] - df[["open", "close"]].max(axis=1)
        res.name = spec.name
        return res


@FeatureRegistry.register
class LowerWickFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "lower_wick"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.PRICE

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        return 1

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        res = df[["open", "close"]].min(axis=1) - df["low"]
        res.name = spec.name
        return res
