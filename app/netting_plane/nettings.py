from typing import Dict, Any
from .models import NettingRecord

class NettingRecordManager:
    def __init__(self):
        self.records: Dict[str, NettingRecord] = {}

    def record_netting(self, data: Dict[str, Any]) -> NettingRecord:
        record = NettingRecord(**data)
        self.records[record.record_id] = record
        return record
