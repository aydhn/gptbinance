from typing import List
from .models import BackfillRecord
from .exceptions import BackfillViolation


class BackfillManager:
    def __init__(self):
        self._backfills: List[BackfillRecord] = []

    def record_backfill(self, backfill: BackfillRecord):
        if backfill.start_time >= backfill.end_time:
            raise BackfillViolation("Start time must be before end time")
        self._backfills.append(backfill)

    def list_backfills(self) -> List[BackfillRecord]:
        return self._backfills
