from typing import Dict, List, Optional
from .models import SubdelegationRecord

class SubdelegationManager:
    """
    Manages subdelegations explicitly to prevent infinite chains and leaked authority.
    """
    def __init__(self):
        self.records: Dict[str, SubdelegationRecord] = {}

    def add_subdelegation(self, sub_id: str, del_id: str, permitted: bool, warnings: List[str] = None) -> SubdelegationRecord:
        record = SubdelegationRecord(sub_id, del_id, permitted, warnings or [], [])
        self.records[sub_id] = record
        return record

    def get_permitted(self) -> List[SubdelegationRecord]:
        return [r for r in self.records.values() if r.permitted]

    def get_prohibited(self) -> List[SubdelegationRecord]:
        return [r for r in self.records.values() if not r.permitted and not r.warnings]

    def get_leaked(self) -> List[SubdelegationRecord]:
        return [r for r in self.records.values() if "LEAKED" in r.warnings]
