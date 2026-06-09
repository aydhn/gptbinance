from typing import Dict, Any, List
from app.oversight_plane.models import OversightRecord
from app.oversight_plane.exceptions import InvalidOversightObjectError

class CanonicalOversightRegistry:
    def __init__(self):
        self._records: Dict[str, OversightRecord] = {}

    def register_oversight(self, oversight_record: OversightRecord):
        if not oversight_record.oversight_id:
            raise InvalidOversightObjectError("Oversight ID is required.")
        self._records[oversight_record.oversight_id] = oversight_record

    def get_oversight(self, oversight_id: str) -> OversightRecord:
        return self._records.get(oversight_id)

    def list_oversight(self) -> List[OversightRecord]:
        return list(self._records.values())

oversight_registry = CanonicalOversightRegistry()
