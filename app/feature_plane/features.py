from typing import Dict, List, Optional
from app.feature_plane.models import FeatureDefinition
from app.feature_plane.base import FeatureRegistryBase
from app.feature_plane.exceptions import InvalidFeatureDefinitionError


class CanonicalFeatureRegistry(FeatureRegistryBase):
    def __init__(self):
        self._features: Dict[str, FeatureDefinition] = {}

    def register(self, feature: FeatureDefinition) -> None:
        if not feature.feature_id:
            raise InvalidFeatureDefinitionError("Feature must have an ID")
        if feature.feature_id in self._features:
            raise InvalidFeatureDefinitionError(
                f"Feature {feature.feature_id} already registered"
            )
        self._features[feature.feature_id] = feature

    def get(self, feature_id: str) -> Optional[FeatureDefinition]:
        return self._features.get(feature_id)

    def list_all(self) -> List[FeatureDefinition]:
        return list(self._features.values())
