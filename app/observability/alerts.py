import logging
from typing import Dict, List, Optional, Any
from datetime import datetime, timezone
from app.observability.models import AlertRule, AlertEvent
from app.observability.enums import AlertState
from app.observability.exceptions import InvalidAlertRule


class AlertEngine:
    def trigger_control_alert(self, event_type: str, severity: str, details: dict):
        self.trigger_experiment_alert(severity, f"Control Event: {event_type}", details)

    def trigger_experiment_alert(
        self, severity: str, message: str, context: dict | None = None
    ):
        logging.getLogger(__name__).warning(
            f"ALERT [{severity.upper()}]: {message} - Context: {context}"
        )

    def resolve_experiment_alert(self, alert_id: str):
        logging.getLogger(__name__).info(f"ALERT RESOLVED: {alert_id}")

    def __init__(self):
        self._rules: Dict[str, AlertRule] = {}
        self._active_alerts: Dict[str, AlertEvent] = {}
        self._alert_history: List[AlertEvent] = []

    def register_rule(self, rule: AlertRule) -> None:
        if rule.rule_id in self._rules:
            raise InvalidAlertRule(f"Rule {rule.rule_id} already registered")
        self._rules[rule.rule_id] = rule

    def evaluate_condition(
        self,
        rule_id: str,
        current_value: float,
        evidence: Optional[Dict[str, Any]] = None,
        runbook_ref: Optional[str] = None,
    ) -> None:
        rule = self._rules.get(rule_id)
        if not rule:
            raise InvalidAlertRule(f"Rule {rule_id} not found")

        triggered = False

        if rule.condition_type == "threshold" and rule.threshold_value is not None:
            if current_value > rule.threshold_value:
                triggered = True
        elif rule.condition_type == "stale" and rule.threshold_value is not None:
            if (
                current_value > rule.threshold_value
            ):  # interpreting current_value as age in seconds
                triggered = True

        # Generate alert ID based on rule_id to group occurrences
        alert_id = f"alert_{rule_id}"

        if triggered:
            self._trigger_alert(rule, alert_id, evidence, runbook_ref)
        else:
            self._clear_alert(alert_id)

    def _trigger_alert(
        self,
        rule: AlertRule,
        alert_id: str,
        evidence: Optional[Dict[str, Any]],
        runbook_ref: Optional[str],
    ) -> None:
        now = datetime.now(timezone.utc)
        if alert_id in self._active_alerts:
            alert = self._active_alerts[alert_id]
            alert.last_seen = now
            alert.occurrence_count += 1
            if evidence:
                alert.evidence.update(evidence)
        else:
            alert = AlertEvent(
                alert_id=alert_id,
                rule_id=rule.rule_id,
                component=rule.component,
                severity=rule.severity,
                state=AlertState.OPEN,
                first_seen=now,
                last_seen=now,
                occurrence_count=1,
                evidence=evidence or {},
                runbook_ref=runbook_ref,
            )
            self._active_alerts[alert_id] = alert
            self._alert_history.append(alert)

    def _clear_alert(self, alert_id: str) -> None:
        if alert_id in self._active_alerts:
            alert = self._active_alerts[alert_id]
            alert.state = AlertState.CLEARED
            alert.last_seen = datetime.now(timezone.utc)
            del self._active_alerts[alert_id]

    def get_active_alerts(self) -> List[AlertEvent]:
        return list(self._active_alerts.values())

    def get_alert_history(self) -> List[AlertEvent]:
        return self._alert_history.copy()


engine = AlertEngine()


class AlertManager:
    def trigger_alert(self, severity: str, message: str, context: dict | None = None):
        logging.getLogger(__name__).warning(
            f"ALERT [{severity.upper()}]: {message} - Context: {context}"
        )

    def resolve_alert(self, alert_id: str):
        logging.getLogger(__name__).info(f"ALERT RESOLVED: {alert_id}")
