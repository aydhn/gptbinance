from typing import Dict, List
from app.program_plane.models import HandoffRecord
from app.program_plane.exceptions import InvalidHandoffState

class HandoffGovernance:
    def __init__(self):
        self._handoffs: Dict[str, HandoffRecord] = {}

    def register(self, handoff: HandoffRecord):
        self._handoffs[handoff.handoff_id] = handoff

    def accept_handoff(self, handoff_id: str):
        if handoff_id in self._handoffs:
            self._handoffs[handoff_id].state = "accepted"
