from typing import Dict, Optional
from .models import DataSchema
from .exceptions import InvalidFieldSchema


class CanonicalSchemaRegistry:
    def __init__(self):
        self._schemas: Dict[str, DataSchema] = {}

    def register(self, schema: DataSchema):
        if not schema.schema_id:
            raise InvalidFieldSchema("Schema ID is required")
        self._schemas[schema.schema_id] = schema

    def get(self, schema_id: str) -> Optional[DataSchema]:
        return self._schemas.get(schema_id)

    def list_all(self) -> list[DataSchema]:
        return list(self._schemas.values())
