import pytest
import pandas as pd
import numpy as np
from app.research.features.engine import FeatureEngine
from app.research.features.models import FeatureRequest, FeatureSpec, WindowConfig
from app.research.features.enums import FeatureCategory
import app.research.features.price_features  # To register them


def get_test_data():
    dates = pd.date_range("2023-01-01", periods=10, freq="15min")
    return pd.DataFrame(
        {
            "open": [10, 11, 12, 11, 10, 9, 8, 9, 10, 11],
            "high": [12, 13, 14, 13, 12, 11, 10, 11, 12, 13],
            "low": [9, 10, 11, 10, 9, 8, 7, 8, 9, 10],
            "close": [11, 12, 11, 10, 9, 8, 9, 10, 11, 12],
            "volume": [100] * 10,
        },
        index=dates,
    )


def test_feature_engine_basic():
    df = get_test_data()
    specs = [
        FeatureSpec(
            name="return", category=FeatureCategory.PRICE, params={"periods": 1}
        ),
        FeatureSpec(name="candle_body", category=FeatureCategory.PRICE),
    ]
    req = FeatureRequest(
        feature_set_name="test_set", symbol="BTC", interval="15m", specs=specs
    )

    engine = FeatureEngine()
    result_df, feature_set = engine.generate(df, req)

    assert "return_1" in result_df.columns
    assert "candle_body" in result_df.columns

    assert len(result_df) == len(df)
    assert result_df.index.equals(df.index)

    assert feature_set.name == "test_set"
    assert feature_set.report.lineage.symbol == "BTC"
