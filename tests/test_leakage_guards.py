import pytest
import pandas as pd
from app.research.features.leakage_guards import LeakageGuard
from app.research.features.exceptions import LeakageError


def test_leakage_guard_index_mismatch():
    df = pd.DataFrame({"close": [1, 2, 3]})
    series = pd.Series([1, 2, 3], index=[1, 2, 3])  # Mismatched index

    with pytest.raises(LeakageError):
        LeakageGuard.check_future_leak(df, series)


def test_validate_warmup():
    series = pd.Series([None, None, 1, 2, 3])
    warmup = LeakageGuard.validate_warmup(series, 2)
    assert warmup == 2
