from typing import Dict, Any
from .models import SetoffRightRecord

class SetoffRightsManager:
    def __init__(self):
        self.records: Dict[str, SetoffRightRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> SetoffRightRecord:
        rec = SetoffRightRecord(**data)
        self.records[rec.setoff_id] = rec
        return rec
