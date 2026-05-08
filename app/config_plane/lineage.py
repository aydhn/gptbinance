from typing import Dict
from app.config_plane.models import EffectiveConfigManifest, ConfigLineageRecord


def get_lineage_for_param(
    manifest: EffectiveConfigManifest, param_key: str
) -> ConfigLineageRecord:
    entry = manifest.entries.get(param_key)
    if not entry:
        return None
    return entry.lineage
