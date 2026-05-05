class SafeRepairPlanner:
    def suggest_repair(self, divergence_type: str) -> str:
        if divergence_type == "SNAPSHOT_MISMATCH_GAP":
            return "refresh_market_truth_snapshot"
        elif divergence_type == "STALLED_FEED":
            return "resubscribe_market_stream"
        elif divergence_type == "DEGRADED":
            return "quarantine_symbol_due_to_data_truth"
        return "request_market_data_review"
