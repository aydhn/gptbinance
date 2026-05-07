from typing import Dict, Optional
from app.feature_plane.models import FeatureSchemaDef
from app.feature_plane.exceptions import FeaturePlaneError


class FeatureSchemaDefRegistry:
    def __init__(self):
        self._schemas: Dict[str, FeatureSchemaDef] = {}

    def register(self, schema: FeatureSchemaDef) -> None:
        if schema.schema_id in self._schemas:
            raise FeaturePlaneError(f"Schema {schema.schema_id} already exists")
        self._schemas[schema.schema_id] = schema

    def get(self, schema_id: str) -> Optional[FeatureSchemaDef]:
        return self._schemas.get(schema_id)
