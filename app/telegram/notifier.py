# Mock implementation
class TelegramNotifier:
    pass

# --- CONFIGURATION PLANE INTEGRATION ---
from app.config_plane.models import EffectiveConfigManifest, ConfigDriftFinding

class ConfigPlaneTelegramNotifier:
    def notify_effective_config_ready(self, manifest: EffectiveConfigManifest):
        print(f"[TELEGRAM] Effective config ready. Hash: {manifest.config_hash}")

    def notify_drift_detected(self, finding: ConfigDriftFinding):
        print(f"[TELEGRAM] DRIFT DETECTED! Parameter {finding.parameter_ref.name} expected {finding.expected_value} got {finding.actual_value}")
