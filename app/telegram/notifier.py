class TelegramNotifier:
    def notify(self, event_type: str, message: str):
        valid_events = [
            "semantic_manifest_ready",
            "semantic_conflict_detected",
            "dangerous_alias_detected",
            "unit_mismatch_detected",
            "semantic_review_required",
            "semantic_summary_digest"
        ]
        if event_type in valid_events:
            print(f"[Telegram Notify] [{event_type}] {message}")
        else:
            print(f"[Telegram Notify] General Message: {message}")
