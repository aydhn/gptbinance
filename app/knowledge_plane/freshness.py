from datetime import datetime, timezone
from .models import FreshnessRecord
from .enums import FreshnessClass

class FreshnessHandling:
    def __init__(self):
        self._records = {}

    def register(self, record: FreshnessRecord):
        self._records[record.knowledge_id] = record

    def get(self, knowledge_id: str) -> FreshnessRecord:
        return self._records.get(knowledge_id)

    def evaluate(self, knowledge_id: str) -> str:
        record = self.get(knowledge_id)
        if not record:
            return FreshnessClass.STALE.value

        now = datetime.now(timezone.utc)
        if now > record.next_review_due:
            return FreshnessClass.EXPIRED.value

        return record.status
