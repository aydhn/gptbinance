class TelegramNotifier:
    EVENT_TYPES = [
        "performance_security_manifest_ready",
        "material_undersecurity_detected",
        "phantom_collateral_detected",
        "premature_security_release_detected",
        "performance_security_review_required"
    ]

    def notify(self, event_type: str, data: dict):
        pass
