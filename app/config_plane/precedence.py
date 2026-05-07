from app.config_plane.models import ConfigOverride
from app.config_plane.layers import ConfigLayerRegistry
from typing import List


class PrecedenceEngine:
    def __init__(self, registry: ConfigLayerRegistry):
        self.registry = registry

    def resolve_winning_override(
        self, overrides: List[ConfigOverride]
    ) -> ConfigOverride:
        if not overrides:
            return None
        return max(
            overrides,
            key=lambda o: self.registry.get_layer(o.layer_class).precedence_order,
        )
