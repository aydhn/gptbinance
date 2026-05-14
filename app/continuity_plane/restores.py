from typing import Dict, List, Optional
from app.continuity_plane.models import RestoreRecord

class RestoreManager:
    def __init__(self):
        self._restores: Dict[str, RestoreRecord] = {}

    def record_restore(self, record: RestoreRecord) -> None:
        self._restores[record.restore_id] = record

    def get_restore(self, restore_id: str) -> Optional[RestoreRecord]:
        return self._restores.get(restore_id)

    def list_restores(self) -> List[RestoreRecord]:
        return list(self._restores.values())
