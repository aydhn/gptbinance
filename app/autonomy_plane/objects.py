from app.autonomy_plane.models import AutonomyObject
from app.autonomy_plane.enums import AutonomyClass

def create_autonomy_object(autonomy_id: str, agent_id: str, autonomy_class: AutonomyClass, owner: str) -> AutonomyObject:
    return AutonomyObject(
        autonomy_id=autonomy_id,
        agent_id=agent_id,
        autonomy_class=autonomy_class,
        owner=owner,
        authorization_posture="unverified",
        intervention_posture="unknown"
    )
