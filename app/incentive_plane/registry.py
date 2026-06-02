from typing import Dict
from app.incentive_plane.models import IncentiveRecord

class CanonicalIncentiveRegistry:
    def __init__(self):
        self.records: Dict[str, IncentiveRecord] = {}

    def register(self, record: IncentiveRecord):
        self.records[record.id] = record

    def get(self, record_id: str) -> IncentiveRecord:
        return self.records.get(record_id)
