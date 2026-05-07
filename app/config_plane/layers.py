from typing import Dict, List
from app.config_plane.models import ConfigLayer, LayerClass
from app.config_plane.enums import ScopeClass


class ConfigLayerRegistry:
    def __init__(self):
        self._layers: Dict[LayerClass, ConfigLayer] = {}
        self._setup_defaults()

    def _setup_defaults(self):
        self.register(
            ConfigLayer(
                layer_id="l_base",
                layer_class=LayerClass.BASE_DEFAULTS,
                allowed_scopes=[ScopeClass.GLOBAL],
                precedence_order=10,
            )
        )
        self.register(
            ConfigLayer(
                layer_id="l_ws",
                layer_class=LayerClass.WORKSPACE_DEFAULTS,
                allowed_scopes=[ScopeClass.WORKSPACE],
                precedence_order=20,
            )
        )
        self.register(
            ConfigLayer(
                layer_id="l_prof",
                layer_class=LayerClass.PROFILE_DEFAULTS,
                allowed_scopes=[ScopeClass.PROFILE],
                precedence_order=30,
            )
        )
        self.register(
            ConfigLayer(
                layer_id="l_sym",
                layer_class=LayerClass.SYMBOL_OVERRIDES,
                allowed_scopes=[ScopeClass.SYMBOL],
                precedence_order=40,
            )
        )
        self.register(
            ConfigLayer(
                layer_id="l_cand",
                layer_class=LayerClass.CANDIDATE_BUNDLE,
                allowed_scopes=[ScopeClass.STAGE],
                precedence_order=50,
            )
        )
        self.register(
            ConfigLayer(
                layer_id="l_deg",
                layer_class=LayerClass.DEGRADED_MODE_OVERLAY,
                allowed_scopes=[ScopeClass.GLOBAL, ScopeClass.PROFILE],
                precedence_order=80,
            )
        )
        self.register(
            ConfigLayer(
                layer_id="l_inc",
                layer_class=LayerClass.INCIDENT_CONTAINMENT_OVERLAY,
                allowed_scopes=[ScopeClass.GLOBAL],
                precedence_order=90,
            )
        )
        self.register(
            ConfigLayer(
                layer_id="l_patch",
                layer_class=LayerClass.RUNTIME_SAFE_PATCH_INTENT,
                allowed_scopes=[ScopeClass.SESSION],
                precedence_order=100,
            )
        )

    def register(self, layer: ConfigLayer):
        self._layers[layer.layer_class] = layer

    def get_layer(self, cls: LayerClass) -> ConfigLayer:
        return self._layers.get(cls)

    def list_layers(self) -> List[ConfigLayer]:
        return sorted(self._layers.values(), key=lambda x: x.precedence_order)
