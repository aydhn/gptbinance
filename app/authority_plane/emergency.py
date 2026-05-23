from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import EmergencyAuthorityRecord

class EmergencyManager:
    def __init__(self):
        self.records: Dict[str, EmergencyAuthorityRecord] = {}

    def get_break_glass(self) -> List[EmergencyAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "BREAK_GLASS"]

    def get_incident(self) -> List[EmergencyAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "INCIDENT"]

    def get_crisis(self) -> List[EmergencyAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "CRISIS"]
