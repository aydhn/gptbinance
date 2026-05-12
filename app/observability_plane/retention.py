from typing import Dict, List, Optional
from .models import RetentionRecord
from .exceptions import RetentionViolationError

class RetentionRegistry:
    def __init__(self):
        self._retention: Dict[str, RetentionRecord] = {}

    def register_retention(self, record: RetentionRecord) -> None:
        if record.retention_days < 1:
            raise RetentionViolationError("Retention must be at least 1 day.")
        self._retention[record.telemetry_id] = record

    def get_retention(self, telemetry_id: str) -> Optional[RetentionRecord]:
        return self._retention.get(telemetry_id)

    def list_retention(self) -> List[RetentionRecord]:
        return list(self._retention.values())
