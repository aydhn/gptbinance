from typing import Dict, Any
from .models import PaymentNettingRecord

class PaymentNettingManager:
    def __init__(self):
        self.records: Dict[str, PaymentNettingRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> PaymentNettingRecord:
        rec = PaymentNettingRecord(**data)
        self.records[rec.payment_netting_id] = rec
        return rec
