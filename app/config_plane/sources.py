from app.config_plane.models import ConfigSourceRecord


class ConfigSourceManager:
    def __init__(self):
        self._sources = {}

    def register_source(self, source: ConfigSourceRecord):
        self._sources[source.source_id] = source
