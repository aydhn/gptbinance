class RemediationTemplates:
    def get_remediation_summary_digest(self):
        pass


class PolicyTemplates:
    def get_policy_hard_block_triggered_template(self):
        return "🚨 POLICY HARD BLOCK 🚨\nAction: {action}\nReason: {reason}"

    def get_conflicting_rules_detected_template(self):
        return (
            "⚠️ CONFLICTING RULES DETECTED ⚠️\nAction: {action}\nConflicts: {conflicts}"
        )

    def get_stale_waiver_warning_template(self):
        return "⚠️ STALE WAIVER WARNING ⚠️\nWaiver {waiver_id} has expired."

    def get_policy_drift_critical_template(self):
        return "🚨 CRITICAL POLICY DRIFT 🚨\nModule: {module}\nExpected: {expected}\nActual: {actual}"

    def get_policy_review_required_template(self):
        return "⚠️ POLICY REVIEW REQUIRED ⚠️\nContext: {context}"

    def get_policy_decision_summary_template(self):
        return "ℹ️ POLICY DECISION SUMMARY ℹ️\nAction: {action}\nVerdict: {verdict}"
