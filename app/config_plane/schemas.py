from typing import Dict, List
from app.config_plane.models import ConfigSchema, ConfigDomain
from app.config_plane.exceptions import InvalidConfigSchema


class CanonicalSchemaRegistry:
    def __init__(self):
        self._schemas: Dict[ConfigDomain, ConfigSchema] = {}

    def register(self, schema: ConfigSchema):
        self._schemas[schema.domain] = schema

    def get_schema(self, domain: ConfigDomain) -> ConfigSchema:
        if domain not in self._schemas:
            raise InvalidConfigSchema(f"Schema not found for domain {domain}")
        return self._schemas[domain]

    def list_schemas(self) -> List[ConfigSchema]:
        return list(self._schemas.values())
