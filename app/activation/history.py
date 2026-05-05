from typing import Dict, Any
import uuid
from app.activation.models import ActivationHistoryRecord


class HistoryTracker:
    def __init__(self, repository):
        self.repository = repository

    def record_event(self, intent_id: str, event_type: str, details: Dict[str, Any]):
        record = ActivationHistoryRecord(
            record_id=f"hist-{uuid.uuid4().hex[:8]}",
            intent_id=intent_id,
            event_type=event_type,
            details=details,
        )
        self.repository.append_history(record)
