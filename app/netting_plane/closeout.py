from typing import Dict, Any
from .models import CloseoutValuationRecord
from .base import CloseoutEvaluatorBase

class CloseoutEvaluator(CloseoutEvaluatorBase):
    def __init__(self):
        self.records: Dict[str, CloseoutValuationRecord] = {}

    def evaluate(self, closeout_id: str, context: Dict[str, Any]) -> Dict[str, Any]:
        rec = CloseoutValuationRecord(closeout_id=closeout_id, status=context.get('status'))
        self.records[closeout_id] = rec
        return rec.model_dump()
