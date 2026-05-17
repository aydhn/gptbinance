from typing import Dict, Optional
from .models import UsabilityReport

class UsabilityReports:
    def __init__(self):
        self._records: Dict[str, UsabilityReport] = {}

    def register(self, record: UsabilityReport):
        self._records[record.knowledge_id] = record

    def get(self, knowledge_id: str) -> Optional[UsabilityReport]:
        return self._records.get(knowledge_id)

    def check_usability(self, knowledge_id: str) -> bool:
        record = self.get(knowledge_id)
        if not record:
            return False
        return record.is_usable
