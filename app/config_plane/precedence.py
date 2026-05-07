from typing import List, Dict, Any, Tuple
from app.config_plane.models import ConfigSourceRecord, ConfigOverride
from app.config_plane.layers import layer_registry

def sort_sources_by_precedence(sources: List[ConfigSourceRecord]) -> List[ConfigSourceRecord]:
    """
    Sorts sources from lowest priority (base) to highest priority (patch).
    This ensures that when iterating and updating a dict, the highest priority wins.
    """
    def get_priority(source: ConfigSourceRecord) -> int:
        layer = layer_registry.get_layer(source.layer_id)
        return layer.priority if layer else 9999

    # Sort descending by priority number (e.g. 1000 -> 100), meaning higher number is resolved first
    return sorted(sources, key=get_priority, reverse=True)
