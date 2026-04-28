import pytest
from app.backtest.validation.sample_splits import SampleSplitter
from app.backtest.validation.enums import SampleSplitType


def test_sample_splitter():
    splitter = SampleSplitter()
    plan = splitter.create_simple_split("BTCUSDT", "1h", 0, 1000, 0.7)
    assert len(plan.windows) == 2
    assert plan.windows[0].split_type == SampleSplitType.IN_SAMPLE
    assert plan.windows[1].split_type == SampleSplitType.OUT_OF_SAMPLE
