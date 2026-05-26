# triggers.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import DistressTriggerRecord
from app.insolvency_plane.enums import DistressTriggerClass

class DistressTriggerManager:
    def __init__(self):
        self.triggers: Dict[str, DistressTriggerRecord] = {}

    def add_trigger(self, trigger: DistressTriggerRecord):
        self.triggers[trigger.trigger_id] = trigger

    def get_trigger(self, trigger_id: str) -> Optional[DistressTriggerRecord]:
        return self.triggers.get(trigger_id)

    def list_triggers(self) -> List[DistressTriggerRecord]:
        return list(self.triggers.values())
