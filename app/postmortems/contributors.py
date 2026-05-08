class PostmortemContributors:
    def add_allocation_contributor(self, factor: str):
        # E.g. wrong_sleeve_routing, stale_sleeve_budget
        pass

class ExecutionContributors:
    CONTRIBUTORS = [
        "stale_venue_filter",
        "duplicate_send_path",
        "hidden_aggressive_routing",
        "cancel_replace_ambiguity",
        "slippage_cluster",
        "passive_postonly_rejection_churn"
    ]
