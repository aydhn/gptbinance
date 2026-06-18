from typing import Dict, Any
from .models import MistakenSetoffRecord

class MistakenSetoffManager:
    def __init__(self):
        self.records: Dict[str, MistakenSetoffRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> MistakenSetoffRecord:
        rec = MistakenSetoffRecord(**data)
        self.records[rec.mistaken_id] = rec
        return rec
