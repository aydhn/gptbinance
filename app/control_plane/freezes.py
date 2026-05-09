import uuid
from typing import Dict, List
from app.control_plane.models import FreezeRecord
from app.control_plane.enums import ScopeClass


class FreezeManager:
    def __init__(self):
        self._freezes: Dict[str, FreezeRecord] = {}

    def freeze_scope(
        self, scope_class: ScopeClass, scope_ref: str, actor: str
    ) -> FreezeRecord:
        record = FreezeRecord(
            freeze_id=f"FRZ-{uuid.uuid4().hex[:8]}",
            scope_class=scope_class,
            scope_ref=scope_ref,
            actor=actor,
        )
        self._freezes[record.freeze_id] = record
        return record

    def get_active_freezes(self) -> List[FreezeRecord]:
        return [f for f in self._freezes.values() if f.is_active]
