from app.environment_plane.models import IsolationRecord
from app.environment_plane.enums import IsolationClass

def define_isolation(isolation_class: IsolationClass, proof_notes: str) -> IsolationRecord:
    return IsolationRecord(isolation_class=isolation_class, proof_notes=proof_notes)


# -- Federation Plane Additions --
def verify_federated_isolation(is_local_isolated: bool, federated_isolation_strength: str) -> str:
    if is_local_isolated and federated_isolation_strength == "weak":
        return "caution: local isolated but federated weak isolation"
    return "trusted"
