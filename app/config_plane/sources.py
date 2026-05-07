from typing import Dict, Any, Optional
from datetime import datetime, timezone
import uuid
from app.config_plane.models import ConfigSourceRecord, ConfigScope
from app.config_plane.enums import LayerClass

class ConfigSourceFactory:
    @staticmethod
    def create_source(
        layer_id: str,
        scope: ConfigScope,
        payload: Dict[str, Any]
    ) -> ConfigSourceRecord:
        return ConfigSourceRecord(
            source_id=f"src_{uuid.uuid4().hex[:8]}",
            layer_id=layer_id,
            scope=scope,
            payload=payload,
            loaded_at=datetime.now(timezone.utc)
        )

# A simple in-memory repository for sources for this phase
class SourceRepository:
    def __init__(self):
        self._sources: Dict[str, ConfigSourceRecord] = {}

    def add_source(self, source: ConfigSourceRecord):
        self._sources[source.source_id] = source

    def get_source(self, source_id: str) -> Optional[ConfigSourceRecord]:
        return self._sources.get(source_id)

    def list_sources(self) -> list[ConfigSourceRecord]:
        return list(self._sources.values())

source_repository = SourceRepository()
