from app.autonomy_plane.registry import registry
from app.autonomy_plane.models import AutonomyObject

class AutonomyRepository:
    def save(self, obj: AutonomyObject) -> None:
        registry.register(obj)

    def get(self, autonomy_id: str) -> AutonomyObject:
        return registry.get(autonomy_id)

repository = AutonomyRepository()
