from typing import List, Optional
from .models import ApplicabilityRecord

class ApplicabilityMappings:
    def __init__(self):
        self._records = {}

    def register(self, record: ApplicabilityRecord):
        self._records[record.knowledge_id] = record

    def get(self, knowledge_id: str) -> ApplicabilityRecord:
        return self._records.get(knowledge_id)

    def evaluate(self, knowledge_id: str, env: Optional[str] = None, role: Optional[str] = None, workflow: Optional[str] = None) -> bool:
        record = self.get(knowledge_id)
        if not record:
            return False

        if env and env not in record.applicable_environments and "all" not in record.applicable_environments:
            return False

        if role and role not in record.applicable_roles and "all" not in record.applicable_roles:
            return False

        if workflow and workflow not in record.applicable_workflows and "all" not in record.applicable_workflows:
            return False

        return True
