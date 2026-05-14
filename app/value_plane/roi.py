from typing import Dict, List, Optional
from app.value_plane.models import RoiRecord
from app.value_plane.exceptions import InvalidRoiRecord

class RoiRegistry:
    def __init__(self):
        self._records: Dict[str, RoiRecord] = {}

    def register(self, record: RoiRecord):
        if not record.cost_linkage:
            raise InvalidRoiRecord("ROI record must have cost linkage.")
        self._records[record.roi_id] = record

    def get(self, record_id: str) -> Optional[RoiRecord]:
        return self._records.get(record_id)

    def list_all(self) -> List[RoiRecord]:
        return list(self._records.values())

roi_registry = RoiRegistry()
