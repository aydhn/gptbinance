from typing import Dict, List, Optional
from .models import SeparationOfDutiesRecord

class SoDManager:
    """
    Tracks separation of duties discipline to avoid single-actor overrides or unchecked controls.
    """
    def __init__(self):
        self.records: Dict[str, SeparationOfDutiesRecord] = {}

    def add_sod(self, sod_id: str, stype: str, relax_notes: List[str] = None) -> SeparationOfDutiesRecord:
        record = SeparationOfDutiesRecord(sod_id, stype, relax_notes or [], [])
        self.records[sod_id] = record
        return record

    def get_maker_checker(self) -> List[SeparationOfDutiesRecord]:
        return [r for r in self.records.values() if r.type == "MAKER_CHECKER"]

    def get_approver_reviewer(self) -> List[SeparationOfDutiesRecord]:
        return [r for r in self.records.values() if r.type == "APPROVER_REVIEWER"]

    def get_financial_control(self) -> List[SeparationOfDutiesRecord]:
        return [r for r in self.records.values() if r.type == "FINANCIAL_CONTROL"]
