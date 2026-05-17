from typing import Dict, List, Optional
from .models import ConflictRecord

class ConflictDetection:
    def __init__(self):
        self._records: Dict[str, ConflictRecord] = {}

    def register(self, record: ConflictRecord):
        self._records[record.knowledge_id] = record

    def get(self, knowledge_id: str) -> Optional[ConflictRecord]:
        return self._records.get(knowledge_id)

    def has_conflicts(self, knowledge_id: str) -> bool:
        record = self.get(knowledge_id)
        if not record:
            return False
        return len(record.conflicts_with) > 0
