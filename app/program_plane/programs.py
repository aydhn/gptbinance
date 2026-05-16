from app.program_plane.models import ProgramRecord
from app.program_plane.registry import CanonicalProgramRegistry

class ProgramManager:
    def __init__(self, registry: CanonicalProgramRegistry):
        self.registry = registry

    def create_program(self, record: ProgramRecord):
        self.registry.register(record)
