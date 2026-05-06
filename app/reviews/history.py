from app.reviews.models import ReviewHistoryRecord
import uuid
from typing import Dict, Any


class HistoryEngine:
    def record_event(
        self,
        item_id: str,
        event_type: str,
        actor_id: str,
        details: Dict[str, Any] = None,
    ) -> ReviewHistoryRecord:
        return ReviewHistoryRecord(
            record_id=str(uuid.uuid4()),
            item_id=item_id,
            event_type=event_type,
            actor_id=actor_id,
            details=details or {},
        )
