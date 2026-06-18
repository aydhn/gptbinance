from typing import Dict, Any
from .models import ObligationEligibilityRecord

class EligibilityManager:
    def __init__(self):
        self.eligibility: Dict[str, ObligationEligibilityRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> ObligationEligibilityRecord:
        rec = ObligationEligibilityRecord(**data)
        self.eligibility[rec.eligibility_id] = rec
        return rec
