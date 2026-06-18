from typing import Dict, Any
from .models import CrossProductNettingRecord

class CrossProductManager:
    def __init__(self):
        self.records: Dict[str, CrossProductNettingRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> CrossProductNettingRecord:
        rec = CrossProductNettingRecord(**data)
        self.records[rec.cross_product_id] = rec
        return rec
