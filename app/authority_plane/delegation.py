from typing import Dict, List, Optional
from .models import DelegationRecord
from .enums import DelegationClass

class DelegationManager:
    """
    Manages delegations strictly tracking scope, temporary state, emergency use,
    and highlighting silent delegations (anomalies).
    """
    def __init__(self):
        self.records: Dict[str, DelegationRecord] = {}

    def add_delegation(self, delegation_id: str, from_auth: str, to_auth: str, dclass: DelegationClass, warnings: List[str] = None) -> DelegationRecord:
        record = DelegationRecord(delegation_id, from_auth, to_auth, dclass, warnings or [], [])
        self.records[delegation_id] = record
        return record

    def get_scoped(self) -> List[DelegationRecord]:
        return [r for r in self.records.values() if r.class_type == DelegationClass.SCOPED]

    def get_temporary(self) -> List[DelegationRecord]:
        return [r for r in self.records.values() if r.class_type == DelegationClass.TEMPORARY]

    def get_emergency(self) -> List[DelegationRecord]:
        return [r for r in self.records.values() if r.class_type == DelegationClass.EMERGENCY]

    def get_task_specific(self) -> List[DelegationRecord]:
        return [r for r in self.records.values() if r.class_type == DelegationClass.TASK_SPECIFIC]

    def get_silent(self) -> List[DelegationRecord]:
        return [r for r in self.records.values() if r.class_type == DelegationClass.SILENT]


def check_waiver_authority_rights(action: str, standing_ref: str, rights_registry) -> str:
    """Verifies if a representative has valid standing to waive rights."""
    if not standing_ref or not rights_registry.is_standing_valid(standing_ref):
        return "explicit caution: waived right by non-authorized representative"
    return "trusted"
