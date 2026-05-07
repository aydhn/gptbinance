from typing import List, Dict
from app.config_plane.models import ConfigLayer
from app.config_plane.enums import LayerClass, ScopeClass

# Deterministic registry of layers with precedence
# Lower precedence number = higher priority during resolution
# Base layer has highest number (lowest priority)
# Patch intent has lowest number (highest priority)

DEFAULT_LAYERS = [
    ConfigLayer(
        layer_id="base_defaults_1",
        layer_class=LayerClass.BASE_DEFAULTS,
        priority=1000,
        allowed_scopes=[ScopeClass.GLOBAL]
    ),
    ConfigLayer(
        layer_id="workspace_defaults_1",
        layer_class=LayerClass.WORKSPACE_DEFAULTS,
        priority=900,
        allowed_scopes=[ScopeClass.WORKSPACE]
    ),
    ConfigLayer(
        layer_id="profile_defaults_1",
        layer_class=LayerClass.PROFILE_DEFAULTS,
        priority=800,
        allowed_scopes=[ScopeClass.PROFILE]
    ),
    ConfigLayer(
        layer_id="candidate_bundle_1",
        layer_class=LayerClass.CANDIDATE_BUNDLE,
        priority=700,
        allowed_scopes=[ScopeClass.CANDIDATE]
    ),
    ConfigLayer(
        layer_id="symbol_overrides_1",
        layer_class=LayerClass.SYMBOL_OVERRIDES,
        priority=600,
        allowed_scopes=[ScopeClass.SYMBOL]
    ),
    ConfigLayer(
        layer_id="degraded_mode_overlay_1",
        layer_class=LayerClass.DEGRADED_MODE_OVERLAY,
        priority=500,
        allowed_scopes=[ScopeClass.GLOBAL, ScopeClass.PROFILE]
    ),
    ConfigLayer(
        layer_id="incident_containment_overlay_1",
        layer_class=LayerClass.INCIDENT_CONTAINMENT_OVERLAY,
        priority=400,
        allowed_scopes=[ScopeClass.GLOBAL, ScopeClass.PROFILE, ScopeClass.SYMBOL]
    ),
    ConfigLayer(
        layer_id="runtime_safe_patch_intent_1",
        layer_class=LayerClass.RUNTIME_SAFE_PATCH_INTENT,
        priority=100,
        allowed_scopes=[ScopeClass.GLOBAL, ScopeClass.PROFILE]
    )
]

class LayerRegistry:
    def __init__(self):
        self._layers: Dict[str, ConfigLayer] = {}
        for layer in DEFAULT_LAYERS:
            self.register_layer(layer)

    def register_layer(self, layer: ConfigLayer):
        self._layers[layer.layer_id] = layer

    def get_layer(self, layer_id: str) -> ConfigLayer:
        return self._layers.get(layer_id)

    def list_layers(self) -> List[ConfigLayer]:
        return sorted(list(self._layers.values()), key=lambda l: l.priority, reverse=True) # Sort lowest priority (highest int) to highest priority (lowest int)

layer_registry = LayerRegistry()
