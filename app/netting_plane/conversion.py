from typing import Dict, Any
from .models import CurrencyConversionRecord

class ConversionManager:
    def __init__(self):
        self.records: Dict[str, CurrencyConversionRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> CurrencyConversionRecord:
        rec = CurrencyConversionRecord(**data)
        self.records[rec.conversion_id] = rec
        return rec
