from typing import Dict, Optional
from app.config_plane.models import ConfigSchema, ConfigParameter, ConfigSchemaVersion
from app.config_plane.enums import ConfigDomain
from app.config_plane.exceptions import InvalidConfigSchema

class SchemaRegistry:
    def __init__(self):
        self._schemas: Dict[ConfigDomain, ConfigSchema] = {}

    def register_schema(self, schema: ConfigSchema) -> None:
        if schema.domain in self._schemas:
            # We could do version checks here, but for simplicity we overwrite/update
            pass
        self._schemas[schema.domain] = schema

    def get_schema(self, domain: ConfigDomain) -> Optional[ConfigSchema]:
        return self._schemas.get(domain)

    def get_parameter(self, domain: ConfigDomain, name: str) -> Optional[ConfigParameter]:
        schema = self.get_schema(domain)
        if not schema:
            return None
        return schema.parameters.get(name)

    def list_schemas(self) -> Dict[ConfigDomain, ConfigSchema]:
        return self._schemas.copy()

registry = SchemaRegistry()
