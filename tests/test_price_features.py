import pytest
import pandas as pd
from app.research.features.price_features import ReturnFeature, CandleBodyFeature
from app.research.features.models import FeatureSpec
from app.research.features.enums import FeatureCategory


def get_test_data():
    return pd.DataFrame(
        {
            "open": [10, 11, 12],
            "high": [12, 13, 14],
            "low": [9, 10, 11],
            "close": [11, 12, 11],
        }
    )


def test_return_feature():
    df = get_test_data()
    spec = FeatureSpec(
        name="return", category=FeatureCategory.PRICE, params={"periods": 1}
    )
    calc = ReturnFeature()

    res = calc(df, spec)
    assert res.iloc[1] == pytest.approx((12 - 11) / 11)
    assert pd.isna(res.iloc[0])


def test_candle_body():
    df = get_test_data()
    spec = FeatureSpec(name="candle_body", category=FeatureCategory.PRICE)
    calc = CandleBodyFeature()

    res = calc(df, spec)
    assert res.iloc[0] == 1  # 11 - 10
    assert res.iloc[2] == -1  # 11 - 12
