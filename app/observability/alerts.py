class AllocationAlerts:
    def trigger_alert(self, alert_type: str):
        # allocation trust degraded, crowding burst detected, capacity clip cluster elevated
        pass

class ExecutionAlerts:
    RULES = [
        "execution_trust_degraded",
        "duplicate_send_detected",
        "venue_filter_integrity_broken",
        "cancel_replace_ambiguity_critical",
        "slippage_cluster_elevated",
        "execution_review_required"
    ]
