from typing import Dict, Any
from .models import ResidualExposureRecord

class ResidualsManager:
    def __init__(self):
        self.records: Dict[str, ResidualExposureRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> ResidualExposureRecord:
        rec = ResidualExposureRecord(**data)
        self.records[rec.residual_id] = rec
        return rec
