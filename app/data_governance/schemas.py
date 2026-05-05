from typing import Dict, Optional, List
from app.data_governance.models import DataSchema, SchemaVersionRef
from app.data_governance.exceptions import InvalidSchemaVersionError
from datetime import datetime, timezone


class SchemaRegistry:
    def __init__(self):
        self._schemas: Dict[str, Dict[str, DataSchema]] = {}

    def register_schema(self, schema: DataSchema) -> None:
        if schema.schema_id not in self._schemas:
            self._schemas[schema.schema_id] = {}
        self._schemas[schema.schema_id][schema.version] = schema

    def get_schema(self, ref: SchemaVersionRef) -> DataSchema:
        if (
            ref.schema_id not in self._schemas
            or ref.version not in self._schemas[ref.schema_id]
        ):
            raise InvalidSchemaVersionError(
                f"Schema {ref.schema_id} version {ref.version} not found"
            )
        return self._schemas[ref.schema_id][ref.version]

    def list_schemas(self) -> List[DataSchema]:
        result = []
        for versions in self._schemas.values():
            result.extend(versions.values())
        return result
