from app.drift_plane.models import RecurrenceTriggerRecord
from app.drift_plane.enums import RecurrenceClass
from typing import Dict
from datetime import datetime

class RecurrenceManager:
    def __init__(self):
        self.triggers: Dict[str, RecurrenceTriggerRecord] = {}

    def add_trigger(self, trigger_id: str, class_type: RecurrenceClass):
        self.triggers[trigger_id] = RecurrenceTriggerRecord(
            trigger_id=trigger_id,
            class_type=class_type,
            triggered_at=datetime.utcnow()
        )

    def get_trigger(self, trigger_id: str) -> RecurrenceTriggerRecord:
        return self.triggers.get(trigger_id)
