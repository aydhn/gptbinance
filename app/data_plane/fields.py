from typing import Dict, Optional
from .models import DataFieldDefinition


class CanonicalFieldRegistry:
    def __init__(self):
        self._fields: Dict[str, DataFieldDefinition] = {}

    def register(self, definition: DataFieldDefinition):
        self._fields[definition.field_name] = definition

    def get(self, field_name: str) -> Optional[DataFieldDefinition]:
        return self._fields.get(field_name)

    def list_all(self) -> list[DataFieldDefinition]:
        return list(self._fields.values())
