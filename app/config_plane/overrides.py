from app.config_plane.models import ConfigOverride


class OverrideManager:
    def __init__(self):
        self._overrides = []

    def add_override(self, override: ConfigOverride):
        self._overrides.append(override)
