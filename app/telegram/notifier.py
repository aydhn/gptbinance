class RemediationNotifier:
    def notify_remediation_blocked(self):
        pass


class PolicyNotifier:
    def notify_policy_hard_block_triggered(self, details: dict):
        pass

    def notify_conflicting_rules_detected(self, details: dict):
        pass

    def notify_stale_waiver_warning(self, details: dict):
        pass

    def notify_policy_drift_critical(self, details: dict):
        pass

    def notify_policy_review_required(self, details: dict):
        pass

    def notify_policy_decision_summary(self, details: dict):
        pass
