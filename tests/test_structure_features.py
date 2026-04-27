import pytest
import pandas as pd
from app.research.features.structure_features import PivotHighFeature
from app.research.features.models import FeatureSpec
from app.research.features.enums import FeatureCategory


def get_test_data():
    return pd.DataFrame({"high": [10, 11, 15, 12, 10, 16, 14, 13]})


def test_pivot_high():
    df = get_test_data()
    # Looking for a pivot with 2 left, 2 right
    spec = FeatureSpec(
        name="pivot_high",
        category=FeatureCategory.STRUCTURE,
        params={"left": 2, "right": 2},
    )
    calc = PivotHighFeature()

    res = calc(df, spec)
    # The pivot at index 2 (value 15) is higher than [10, 11] and [12, 10]
    # It is confirmed at index 4
    assert res.iloc[4] == 1
    # Index 5 (value 16) is a pivot, confirmed at index 7
    assert res.iloc[7] == 1
    # Others should be 0 or NaN
    assert res.iloc[3] == 0
