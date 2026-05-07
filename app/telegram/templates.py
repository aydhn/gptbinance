# Mock implementation
class TelegramTemplates:
    pass

class FeatureTelegramTemplates:
    def __init__(self):
        self.templates = [
            "feature_manifest_ready",
            "feature_leakage_detected",
            "feature_skew_elevated",
            "feature_integrity_degraded",
            "feature_review_required",
            "feature_summary_digest"
        ]
