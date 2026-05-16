from app.program_plane.models import ReplanRecord
from app.program_plane.exceptions import InvalidReplanRecord

class ReplanGovernance:
    def register_replan(self, record: ReplanRecord):
        if not record.program_id:
            raise InvalidReplanRecord("Missing program id in replan")
