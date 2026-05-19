from typing import Dict, List, Optional
from app.learning_plane.models import LearningObject, LearningPlaneConfig
from app.learning_plane.base import LearningRegistryBase
from app.learning_plane.exceptions import InvalidLearningObject
from app.learning_plane.storage import storage

class CanonicalLearningRegistry(LearningRegistryBase):
    def __init__(self, config: Optional[LearningPlaneConfig] = None):
        self.config = config or LearningPlaneConfig()

    def register_object(self, obj: LearningObject) -> None:
        if not obj.learning_id:
            raise InvalidLearningObject("Learning ID cannot be empty.")

        if self.config.enforce_strict_lineage:
            if not obj.origin_id:
                raise InvalidLearningObject("Origin ID must be provided when strict lineage is enforced.")

        if self.config.require_validation and obj.state == "closed" and not obj.validation_ids:
             raise InvalidLearningObject("Cannot close learning without validation records when validation is required.")

        storage.save_object(obj)

    def get_object(self, learning_id: str) -> LearningObject:
        obj = storage.get_object(learning_id)
        if not obj:
            raise InvalidLearningObject(f"Learning object '{learning_id}' not found in registry.")
        return obj

    def get_all_objects(self) -> List[LearningObject]:
        return list(storage.objects.values())
