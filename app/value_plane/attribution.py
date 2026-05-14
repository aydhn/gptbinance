from typing import Dict, List, Optional
from app.value_plane.models import AttributionRecord

class AttributionRegistry:
    def __init__(self):
        self._records: Dict[str, AttributionRecord] = {}

    def register(self, record: AttributionRecord):
        self._records[record.attribution_id] = record

    def get(self, record_id: str) -> Optional[AttributionRecord]:
        return self._records.get(record_id)

    def list_all(self) -> List[AttributionRecord]:
        return list(self._records.values())

attribution_registry = AttributionRegistry()
