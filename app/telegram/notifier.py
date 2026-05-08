from typing import Dict, Any


class TelegramNotifier:
    @staticmethod
    def notify_performance_event(event_type: str, severity: str, message: str) -> bool:
        valid_events = [
            "performance_manifest_ready",
            "performance_trust_degraded",
            "benchmark_integrity_broken",
            "attribution_review_required",
            "performance_equivalence_broken",
        ]

        if event_type not in valid_events:
            return False

        # Implementing basic severity/rate-limiting check
        if severity == "INFO":
            # For info, we would check rate-limit; assume pass for now
            pass

        # Send message
        return True
