from datetime import datetime, timezone, timedelta
from typing import Optional
from app.governance.models import RefreshTrigger
from app.governance.enums import RefreshTriggerType


class TriggerEvaluator:
    def evaluate_time_based(
        self, last_run: Optional[datetime], interval_hours: int
    ) -> bool:
        if last_run is None:
            return True
        return datetime.now(timezone.utc) - last_run > timedelta(hours=interval_hours)

    def create_trigger(
        self, trigger_type: RefreshTriggerType, source: str
    ) -> RefreshTrigger:
        return RefreshTrigger(
            trigger_type=trigger_type,
            source=source,
            timestamp=datetime.now(timezone.utc),
        )


def trigger_downstream_refresh():
    pass
