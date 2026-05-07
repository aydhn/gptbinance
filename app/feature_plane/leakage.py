from app.feature_plane.enums import LeakageSeverity


class LeakageDetector:
    def detect_leakage(self, feature_id: str) -> LeakageSeverity:
        # Dummy implementation
        return LeakageSeverity.NONE
