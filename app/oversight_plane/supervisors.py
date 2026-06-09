from app.oversight_plane.models import SupervisorRecord
from typing import List

_supervisors = {}

def add_supervisor(supervisor_id: str, supervisor_type: str = "direct"):
    _supervisors[supervisor_id] = SupervisorRecord(supervisor_id=supervisor_id, supervisor_type=supervisor_type)
    return _supervisors[supervisor_id]

def get_supervisor(supervisor_id: str) -> SupervisorRecord:
    return _supervisors.get(supervisor_id)
