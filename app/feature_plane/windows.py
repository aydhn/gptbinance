from app.feature_plane.models import FeatureWindow
from datetime import timedelta


class WindowUtils:
    @staticmethod
    def is_valid_window(window: FeatureWindow) -> bool:
        if window.lookback_duration and window.lookback_duration < timedelta(0):
            return False
        if window.lookback_ticks and window.lookback_ticks < 0:
            return False
        return True
