import pandas as pd
import numpy as np

from app.research.features.base import BaseFeatureCalculator
from app.research.features.registry import FeatureRegistry
from app.research.features.models import FeatureSpec
from app.research.features.enums import FeatureCategory
from app.research.features.exceptions import InvalidFeatureSpecError


@FeatureRegistry.register
class RSIFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "rsi"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.OSCILLATOR

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        if not spec.window:
            raise InvalidFeatureSpecError("rsi requires a window configuration")
        return spec.window.window_size + 1

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        if not spec.window:
            raise InvalidFeatureSpecError("rsi requires a window configuration")

        source = spec.params.get("source", "close")
        window_size = spec.window.window_size

        delta = df[source].diff()
        gain = (
            (delta.where(delta > 0, 0)).ewm(alpha=1 / window_size, adjust=False).mean()
        )
        loss = (
            (-delta.where(delta < 0, 0)).ewm(alpha=1 / window_size, adjust=False).mean()
        )

        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))

        # Avoid division by zero
        rsi = (
            rsi.fillna(100)
            .where(loss != 0, 100)
            .where(gain != 0, 0)
            .where((gain != 0) | (loss != 0), 50)
        )

        rsi.name = f"{spec.name}_{window_size}"
        return rsi


@FeatureRegistry.register
class StochasticOscillatorFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "stoch"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.OSCILLATOR

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        if not spec.window:
            raise InvalidFeatureSpecError("stoch requires a window configuration")
        return spec.window.window_size

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        if not spec.window:
            raise InvalidFeatureSpecError("stoch requires a window configuration")

        window_size = spec.window.window_size
        min_periods = spec.window.min_periods

        lowest_low = (
            df["low"].rolling(window=window_size, min_periods=min_periods).min()
        )
        highest_high = (
            df["high"].rolling(window=window_size, min_periods=min_periods).max()
        )

        k = 100 * ((df["close"] - lowest_low) / (highest_high - lowest_low))
        k = k.fillna(50)  # fallback

        k.name = f"{spec.name}_k_{window_size}"
        return k
