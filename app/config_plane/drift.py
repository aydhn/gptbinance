from app.config_plane.models import ConfigDriftFinding, EffectiveConfigManifest


class DriftDetector:
    def detect(
        self, expected: EffectiveConfigManifest, actual: EffectiveConfigManifest
    ) -> list[ConfigDriftFinding]:
        findings = []
        # Mock detection logic
        return findings
