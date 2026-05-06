class ActivationAlerts:
    @staticmethod
    def evaluate_activation_alerts(activation_state: dict):
        alerts = []
        if activation_state.get("probation_failed"):
            alerts.append("ACTIVATION_PROBATION_FAILED")
        if activation_state.get("active_set_conflict"):
            alerts.append("ACTIVE_SET_CONFLICT_DETECTED")
        return alerts


# Exported rules to incident command: Emit alerts on incident escalation