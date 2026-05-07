# Wraps resolution to build immutable effective manifests
from app.config_plane.resolution import ResolutionEngine


class EffectiveConfigBuilder:
    def __init__(self):
        self.engine = ResolutionEngine()
