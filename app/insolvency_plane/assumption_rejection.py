# assumption_rejection.py
from typing import Dict, List, Optional
from pydantic import BaseModel

class AssumptionRejectionRecord(BaseModel):
    record_id: str
    commitment_id: str
    action_type: str # assumed, rejected, conditional, invalid
    description: str
    lineage_refs: List[str]

class AssumptionRejectionManager:
    def __init__(self):
        self.records: Dict[str, AssumptionRejectionRecord] = {}

    def register_action(self, record: AssumptionRejectionRecord):
        self.records[record.record_id] = record

    def get_action(self, record_id: str) -> Optional[AssumptionRejectionRecord]:
        return self.records.get(record_id)

    def list_actions(self) -> List[AssumptionRejectionRecord]:
        return list(self.records.values())
