class IncidentIntake:
    def report_allocation_incident(self, signal: str):
        # allocation_budget_broken, capacity_clip_critical_cluster, crowding_burst_detected, etc.
        pass

class ExecutionIncidentSignals:
    SIGNALS = [
        "duplicate_send_attempt_detected",
        "venue_filter_integrity_broken",
        "cancel_replace_ambiguity_critical",
        "runtime_execution_manifest_missing",
        "execution_equivalence_broken",
        "slippage_cluster_critical"
    ]
