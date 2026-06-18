from typing import Dict, Any
from .models import AntiDuplicationRecord

class AntiDuplicationManager:
    def __init__(self):
        self.records: Dict[str, AntiDuplicationRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> AntiDuplicationRecord:
        rec = AntiDuplicationRecord(**data)
        self.records[rec.anti_duplication_id] = rec
        return rec
