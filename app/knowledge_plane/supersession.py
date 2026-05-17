from typing import Dict, Optional
from .models import SupersessionRecord

class SupersessionGovernance:
    def __init__(self):
        self._records: Dict[str, SupersessionRecord] = {}

    def register(self, record: SupersessionRecord):
        self._records[record.knowledge_id] = record

    def get(self, knowledge_id: str) -> Optional[SupersessionRecord]:
        return self._records.get(knowledge_id)

    def is_superseded(self, knowledge_id: str) -> bool:
        record = self.get(knowledge_id)
        if not record:
            return False
        return bool(record.superseded_by)
