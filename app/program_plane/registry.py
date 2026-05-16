from typing import Dict, List
from app.program_plane.models import ProgramRecord
from app.program_plane.exceptions import InvalidProgramObject

class CanonicalProgramRegistry:
    def __init__(self):
        self._programs: Dict[str, ProgramRecord] = {}

    def register(self, record: ProgramRecord):
        if not record.program_id:
            raise InvalidProgramObject("No undocumented program ids allowed")
        self._programs[record.program_id] = record

    def get(self, program_id: str) -> ProgramRecord:
        return self._programs.get(program_id)

    def list_all(self) -> List[ProgramRecord]:
        return list(self._programs.values())
