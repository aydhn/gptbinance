from typing import Dict, Any
from .models import NettingComparisonRecord

class ComparisonsManager:
    def __init__(self):
        self.records: Dict[str, NettingComparisonRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> NettingComparisonRecord:
        rec = NettingComparisonRecord(**data)
        self.records[rec.comparison_id] = rec
        return rec
