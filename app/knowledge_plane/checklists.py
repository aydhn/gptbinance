from typing import Dict, Optional
from .models import ChecklistRecord

class ChecklistRegistry:
    def __init__(self):
        self._records: Dict[str, ChecklistRecord] = {}

    def register(self, record: ChecklistRecord):
        self._records[record.knowledge_id] = record

    def get(self, knowledge_id: str) -> Optional[ChecklistRecord]:
        return self._records.get(knowledge_id)

    def is_enforced(self, knowledge_id: str) -> bool:
        record = self.get(knowledge_id)
        if not record:
            return False
        return record.enforced
