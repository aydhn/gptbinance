from typing import Dict, List, Optional
from .models import LogSchema
from .exceptions import InvalidSchemaContractError

class LogSchemaRegistry:
    def __init__(self):
        self._schemas: Dict[str, LogSchema] = {}

    def register_schema(self, schema: LogSchema) -> None:
        if not schema.required_fields:
            raise InvalidSchemaContractError("Structured logs must declare required fields.")
        self._schemas[schema.telemetry_id] = schema

    def get_schema(self, telemetry_id: str) -> Optional[LogSchema]:
        return self._schemas.get(telemetry_id)

    def list_schemas(self) -> List[LogSchema]:
        return list(self._schemas.values())
