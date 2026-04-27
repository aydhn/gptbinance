import pytest
import pandas as pd
from app.research.features.divergence import BullishDivergenceCandidateFeature
from app.research.features.models import FeatureSpec
from app.research.features.enums import FeatureCategory


def get_test_data():
    # Construct a scenario for regular bullish divergence
    # Price makes a Lower Low
    # Osc makes a Higher Low

    # We need at least 10 rows to pass the min history check
    df = pd.DataFrame(
        {
            "low": [20, 19, 18, 17, 16, 10, 8, 12, 6, 10],
            "rsi": [50, 45, 40, 35, 30, 30, 20, 50, 25, 40],
        }
    )
    return df


def test_regular_bullish_divergence():
    df = get_test_data()
    spec = FeatureSpec(
        name="bullish_divergence_candidate",
        category=FeatureCategory.DIVERGENCE,
        params={"left": 1, "right": 1, "osc_column": "rsi"},
    )
    calc = BullishDivergenceCandidateFeature()

    res = calc(df, spec)

    assert res.iloc[9] == 1  # 1 = Regular Bullish
