from typing import Dict, Any
from .models import MutualityRecord
from .base import MutualityEvaluatorBase

class MutualityEvaluator(MutualityEvaluatorBase):
    def __init__(self):
        self.records: Dict[str, MutualityRecord] = {}

    def evaluate(self, mutuality_id: str, context: Dict[str, Any]) -> Dict[str, Any]:
        rec = MutualityRecord(mutuality_id=mutuality_id, status=context.get('status'))
        self.records[mutuality_id] = rec
        return rec.model_dump()
