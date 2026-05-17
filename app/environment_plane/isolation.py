from app.environment_plane.models import IsolationRecord
from app.environment_plane.enums import IsolationClass

def define_isolation(isolation_class: IsolationClass, proof_notes: str) -> IsolationRecord:
    return IsolationRecord(isolation_class=isolation_class, proof_notes=proof_notes)
