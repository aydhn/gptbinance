from datetime import datetime, timezone
from app.governance.models import RefreshTrigger
from app.governance.enums import RefreshTriggerType


class TriggerEvaluator:
    def evaluate_time_based(self, last_refresh: datetime, interval_hours: int) -> bool:
        if last_refresh is None:
            return True
        now = datetime.now(timezone.utc)
        return (now - last_refresh).total_seconds() / 3600 >= interval_hours

    def create_trigger(
        self, trigger_type: RefreshTriggerType, source: str, details: dict = None
    ) -> RefreshTrigger:
        return RefreshTrigger(
            trigger_type=trigger_type, source=source, details=details or {}
        )
