from app.environment_plane.models import EnvironmentObject, EnvironmentRecord
from app.environment_plane.enums import EnvironmentClass
from datetime import datetime, timezone

def create_environment_object(env_id: str, env_class: EnvironmentClass, owner: str, description: str) -> EnvironmentObject:
    return EnvironmentObject(
        environment_id=env_id,
        record=EnvironmentRecord(
            id=env_id,
            environment_class=env_class,
            owner=owner,
            description=description,
            created_at=datetime.now(timezone.utc)
        )
    )
