class RemediationAlerts:
    def create_stale_pack_alert(self):
        pass


class PolicyAlerts:
    def trigger_hard_block_bypass_attempt(self, details: dict):
        pass

    def trigger_conflicting_rules_detected(self, details: dict):
        pass

    def trigger_stale_waiver_used(self, details: dict):
        pass

    def trigger_policy_drift_critical(self, details: dict):
        pass

    def trigger_missing_invariant_coverage(self, details: dict):
        pass
