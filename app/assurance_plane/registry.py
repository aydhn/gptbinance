from typing import Dict, Optional, List
from app.assurance_plane.models import AssuranceObject, AssuranceRecord
from app.assurance_plane.base import AssuranceRegistryBase

class AssuranceRegistry(AssuranceRegistryBase):
    def __init__(self):
        self._registry: Dict[str, AssuranceObject] = {}
        self._records: Dict[str, AssuranceRecord] = {}

    def register_assurance(self, obj: AssuranceObject) -> None:
        self._registry[obj.assurance_id] = obj

    def get_assurance_object(self, assurance_id: str) -> Optional[AssuranceObject]:
        return self._registry.get(assurance_id)

    def register_record(self, record: AssuranceRecord) -> None:
        self._records[record.record_id] = record

    def get_assurance(self, record_id: str) -> Optional[AssuranceRecord]:
        return self._records.get(record_id)

    def get_all_records(self) -> List[AssuranceRecord]:
        return list(self._records.values())
