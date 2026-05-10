class TelegramNotifier:
    def send_release_plane_event(self, event_type: str, data: dict):
        valid_events = [
            "release_manifest_ready",
            "release_trust_degraded",
            "hidden_hotfix_detected",
            "rollout_stage_drift_detected",
            "release_review_required"
        ]
        if event_type in valid_events:
            # Enforce severity/rate-limit logic
            # Audit ref inclusion for critical missing events
            pass


class PostmortemTelegramNotifier:
    def notify(self, event_type: str, postmortem_id: str):
        pass
