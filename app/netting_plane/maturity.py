from typing import Dict, Any
from .models import MaturityRecord

class MaturityManager:
    def __init__(self):
        self.records: Dict[str, MaturityRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> MaturityRecord:
        rec = MaturityRecord(**data)
        self.records[rec.maturity_id] = rec
        return rec
