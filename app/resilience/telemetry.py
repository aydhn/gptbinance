import logging
from datetime import datetime, timezone
from typing import Dict, Any, List
from app.resilience.models import ChaosEventRecord

logger = logging.getLogger(__name__)


class ExperimentTelemetry:
    def __init__(self):
        self.events: List[ChaosEventRecord] = []

    def record_event(self, run_id: str, event_type: str, details: Dict[str, Any]):
        event = ChaosEventRecord(
            event_id=f"{run_id}_{len(self.events)}",
            timestamp=datetime.now(timezone.utc),
            event_type=event_type,
            details=details,
        )
        self.events.append(event)
        logger.debug(f"[RESILIENCE TELEMETRY] {event_type} - {details}")

    def get_timeline(self, run_id: str) -> List[ChaosEventRecord]:
        # In reality, would filter by run_id from storage
        return self.events
