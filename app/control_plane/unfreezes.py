from typing import Dict
from app.control_plane.models import UnfreezeRecord


class UnfreezeManager:
    def __init__(self):
        self._unfreezes: Dict[str, UnfreezeRecord] = {}

    def unfreeze(self, freeze_id: str, actor: str, reason: str) -> UnfreezeRecord:
        record = UnfreezeRecord(freeze_id=freeze_id, actor=actor, reason=reason)
        self._unfreezes[freeze_id] = record
        return record
