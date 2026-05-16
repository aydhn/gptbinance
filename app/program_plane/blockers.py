from typing import Dict, List
from app.program_plane.models import BlockerRecord
from app.program_plane.exceptions import InvalidBlockerState

class BlockerHandler:
    def __init__(self):
        self._blockers: Dict[str, BlockerRecord] = {}

    def register(self, blocker: BlockerRecord):
        self._blockers[blocker.blocker_id] = blocker

    def list_active(self, program_id: str) -> List[BlockerRecord]:
        return [b for b in self._blockers.values() if b.program_id == program_id and not b.is_resolved]
