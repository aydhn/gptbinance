from typing import Dict, Any
from .models import StayBlockRecord

class StayBlocksManager:
    def __init__(self):
        self.records: Dict[str, StayBlockRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> StayBlockRecord:
        rec = StayBlockRecord(**data)
        self.records[rec.stay_block_id] = rec
        return rec
