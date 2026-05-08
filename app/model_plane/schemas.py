from typing import Dict, List, Optional
from app.model_plane.models import ModelSchema, OutputSchema, ModelSchemaVersion
from app.model_plane.exceptions import InvalidModelDefinitionError


class ModelSchemaRegistry:
    def __init__(self):
        self._schemas: Dict[str, ModelSchema] = {}
        self._versions: Dict[str, List[ModelSchemaVersion]] = {}

    def register_schema(self, schema: ModelSchema) -> None:
        if not schema.schema_id:
            raise InvalidModelDefinitionError("Schema ID is required.")
        if not schema.input_feature_manifest_id:
            raise InvalidModelDefinitionError("Input feature manifest ID is required.")
        if not schema.output_schema:
            raise InvalidModelDefinitionError("Output schema is required.")

        self._schemas[schema.schema_id] = schema

    def register_version(self, version: ModelSchemaVersion) -> None:
        if not version.schema_id or version.schema_id not in self._schemas:
            raise InvalidModelDefinitionError(
                f"Schema {version.schema_id} must be registered first."
            )

        if version.schema_id not in self._versions:
            self._versions[version.schema_id] = []
        self._versions[version.schema_id].append(version)

    def get_schema(self, schema_id: str) -> Optional[ModelSchema]:
        return self._schemas.get(schema_id)

    def get_versions(self, schema_id: str) -> List[ModelSchemaVersion]:
        return self._versions.get(schema_id, [])
