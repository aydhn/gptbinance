from typing import Optional, List
from app.assurance_plane.registry import AssuranceRegistry
from app.assurance_plane.models import AssuranceRecord

class AssuranceRepository:
    def __init__(self, registry: AssuranceRegistry):
        self.registry = registry

    def save(self, record: AssuranceRecord):
        self.registry.register_record(record)
        self.registry.register_assurance(record.assurance_obj)

    def get(self, assurance_id: str) -> Optional[AssuranceRecord]:
        for rec in self.registry.get_all_records():
            if rec.assurance_obj.assurance_id == assurance_id:
                return rec
        return None

    def list_all(self) -> List[AssuranceRecord]:
        return self.registry.get_all_records()
