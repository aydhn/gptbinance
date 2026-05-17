from typing import Dict, Optional
from .models import StandardRecord

class StandardsRegistry:
    def __init__(self):
        self._records: Dict[str, StandardRecord] = {}

    def register(self, record: StandardRecord):
        self._records[record.knowledge_id] = record

    def get(self, knowledge_id: str) -> Optional[StandardRecord]:
        return self._records.get(knowledge_id)

    def is_mandatory(self, knowledge_id: str) -> bool:
        record = self.get(knowledge_id)
        if not record:
            return False
        return record.is_mandatory
