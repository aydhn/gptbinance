from typing import Dict, List, Optional
from .models import QuorumRecord
from .enums import QuorumClass

class QuorumManager:
    """
    Evaluates quorum states. Fights quorum theater.
    """
    def __init__(self):
        self.records: Dict[str, QuorumRecord] = {}

    def add_quorum(self, q_id: str, qclass: QuorumClass, warnings: List[str] = None) -> QuorumRecord:
        record = QuorumRecord(q_id, qclass, warnings or [], [])
        self.records[q_id] = record
        return record

    def get_satisfied(self) -> List[QuorumRecord]:
        return [r for r in self.records.values() if r.class_type == QuorumClass.SATISFIED]

    def get_partial(self) -> List[QuorumRecord]:
        return [r for r in self.records.values() if r.class_type == QuorumClass.PARTIAL]

    def get_invalid(self) -> List[QuorumRecord]:
        return [r for r in self.records.values() if r.class_type == QuorumClass.INVALID]

    def get_proxy(self) -> List[QuorumRecord]:
        return [r for r in self.records.values() if r.class_type == QuorumClass.PROXY]
