import uuid
from typing import Dict, List
from app.control_plane.models import ScopePauseRecord
from app.control_plane.enums import ScopeClass


class PauseManager:
    def __init__(self):
        self._pauses: Dict[str, ScopePauseRecord] = {}

    def pause_scope(
        self, scope_class: ScopeClass, scope_ref: str, actor: str
    ) -> ScopePauseRecord:
        record = ScopePauseRecord(
            pause_id=f"PAUSE-{uuid.uuid4().hex[:8]}",
            scope_class=scope_class,
            scope_ref=scope_ref,
            actor=actor,
        )
        self._pauses[record.pause_id] = record
        return record

    def get_active_pauses(self) -> List[ScopePauseRecord]:
        return [p for p in self._pauses.values() if p.is_active]
