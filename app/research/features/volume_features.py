import pandas as pd

from app.research.features.base import BaseFeatureCalculator
from app.research.features.registry import FeatureRegistry
from app.research.features.models import FeatureSpec
from app.research.features.enums import FeatureCategory
from app.research.features.exceptions import InvalidFeatureSpecError


@FeatureRegistry.register
class RelativeVolumeFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "relative_volume"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.VOLUME

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        if not spec.window:
            raise InvalidFeatureSpecError(
                "relative_volume requires a window configuration"
            )
        return spec.window.window_size

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        if not spec.window:
            raise InvalidFeatureSpecError(
                "relative_volume requires a window configuration"
            )
        window_size = spec.window.window_size

        # Current volume relative to moving average of volume
        ma_vol = (
            df["volume"]
            .rolling(window=window_size, min_periods=spec.window.min_periods)
            .mean()
        )
        res = df["volume"] / ma_vol
        res.name = f"{spec.name}_{window_size}"
        return res


@FeatureRegistry.register
class VolumeChangeFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "volume_change"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.VOLUME

    @classmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        periods = spec.params.get("periods", 1)
        return periods + 1

    def calculate(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series:
        periods = spec.params.get("periods", 1)
        res = df["volume"].pct_change(periods=periods)
        res.name = f"{spec.name}_{periods}"
        return res
