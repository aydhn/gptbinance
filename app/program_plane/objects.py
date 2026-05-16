from app.program_plane.models import ProgramObject
from app.program_plane.exceptions import InvalidProgramObject

class ProgramObjectManager:
    def validate_object(self, obj: ProgramObject):
        if not obj.program_id or not obj.program_class:
            raise InvalidProgramObject("Program object missing fields")
