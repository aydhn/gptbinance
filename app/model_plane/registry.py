from typing import Dict, List, Optional
from app.model_plane.base import ModelRegistryBase
from app.model_plane.models import ModelDefinition
from app.model_plane.enums import ModelClass
from app.model_plane.exceptions import InvalidModelDefinitionError


class CanonicalModelRegistry(ModelRegistryBase):
    def __init__(self):
        self._models: Dict[str, ModelDefinition] = {}

    def register_model(self, model: ModelDefinition) -> None:
        if not model.model_id:
            raise InvalidModelDefinitionError("Model must have an ID.")

        # Enforce canonical typed model ids - no random unmanaged ids.
        # Check if the class is one of the supported model classes.
        if model.model_class not in ModelClass:
            raise InvalidModelDefinitionError(
                f"Unsupported model class: {model.model_class}"
            )

        self._models[model.model_id] = model

    def get_model(self, model_id: str) -> Optional[ModelDefinition]:
        return self._models.get(model_id)

    def list_models(self) -> List[ModelDefinition]:
        return list(self._models.values())

    def get_models_by_class(self, model_class: ModelClass) -> List[ModelDefinition]:
        return [m for m in self._models.values() if m.model_class == model_class]
