from datetime import datetime
from app.ml.enums import SplitType
from app.ml.splits import SplitEngine


def test_split_engine():
    engine = SplitEngine()
    start = datetime(2023, 1, 1)
    end = datetime(2023, 2, 1)

    plan = engine.create_split_plan(SplitType.ANCHORED, start, end)

    assert plan.split_type == SplitType.ANCHORED
    assert len(plan.train_intervals) == 1
