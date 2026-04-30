from datetime import datetime
from typing import List
from app.ml.models import TemporalSplitPlan
from app.ml.enums import SplitType


class SplitEngine:
    def create_split_plan(
        self, split_type: SplitType, data_start: datetime, data_end: datetime
    ) -> TemporalSplitPlan:
        # temporal split discipline
        # contiguous, anchored, expanding, walk_forward
        # no random shuffle
        return TemporalSplitPlan(
            split_type=split_type,
            train_intervals=[{"start": data_start, "end": data_end}],
            test_intervals=[{"start": data_end, "end": data_end}],
        )
