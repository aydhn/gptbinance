from typing import Dict, Optional
from .models import DataSourceDefinition
from .exceptions import InvalidSourceDefinition


class CanonicalSourceRegistry:
    def __init__(self):
        self._sources: Dict[str, DataSourceDefinition] = {}

    def register(self, definition: DataSourceDefinition):
        if not definition.source_id:
            raise InvalidSourceDefinition("Source ID is required")
        self._sources[definition.source_id] = definition

    def get(self, source_id: str) -> Optional[DataSourceDefinition]:
        return self._sources.get(source_id)

    def list_all(self) -> list[DataSourceDefinition]:
        return list(self._sources.values())
