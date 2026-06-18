from typing import Dict, Any
from .models import ContractualSetoffRecord

class ContractualSetoffManager:
    def __init__(self):
        self.records: Dict[str, ContractualSetoffRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> ContractualSetoffRecord:
        rec = ContractualSetoffRecord(**data)
        self.records[rec.contractual_id] = rec
        return rec
