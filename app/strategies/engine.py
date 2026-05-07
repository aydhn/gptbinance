# Stub for strategy engine integration
def evaluate_strategy_candidates(candidates, truth_verdict):
    if truth_verdict == "BLOCK":
        return []
    return candidates

# --- CONFIGURATION PLANE INTEGRATION ---
from app.config_plane.models import EffectiveConfigManifest

class ConfigAwareStrategyEngine:
    def __init__(self, config_manifest: EffectiveConfigManifest):
        self.config_manifest = config_manifest
        self.effective_refs = config_manifest.manifest_id

    def get_feature_flag(self, flag_name: str) -> bool:
        entry = self.config_manifest.entries.get(f"strategy.{flag_name}")
        return entry.value if entry else False
