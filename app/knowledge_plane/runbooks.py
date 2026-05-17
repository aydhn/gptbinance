from typing import Dict, Optional
from .models import RunbookRecord

class RunbookRegistry:
    def __init__(self):
        self._records: Dict[str, RunbookRecord] = {}

    def register(self, record: RunbookRecord):
        self._records[record.knowledge_id] = record

    def get(self, knowledge_id: str) -> Optional[RunbookRecord]:
        return self._records.get(knowledge_id)
