import re

with open('app/telegram/notifier.py', 'r') as f:
    content = f.read()

patch_methods = """    def notify_health_degraded(self, component: str, severity: str, explanation: str) -> None:
        from app.telegram.templates import render_health_degraded
        self.send_message(render_health_degraded(component, severity, explanation))

    def notify_critical_alert(self, alert_id: str, component: str, rule: str, evidence: dict) -> None:
        from app.telegram.templates import render_critical_alert
        self.send_message(render_critical_alert(alert_id, component, rule, evidence))

    def notify_correlated_incident(self, group_id: str, primary_alert: str, likely_issue: str) -> None:
        from app.telegram.templates import render_correlated_incident
        self.send_message(render_correlated_incident(group_id, primary_alert, likely_issue))

    def notify_slo_breach(self, slo_id: str, current: float, explanation: str) -> None:
        from app.telegram.templates import render_slo_breach
        self.send_message(render_slo_breach(slo_id, current, explanation))

    def notify_observability_digest(self, scope: str, top_alerts: list, highlights: str) -> None:
        from app.telegram.templates import render_observability_digest
        self.send_message(render_observability_digest(scope, top_alerts, highlights))

def get_notifier(config) -> BaseNotifier:"""

content = content.replace("def get_notifier(config) -> BaseNotifier:", patch_methods)

with open('app/telegram/notifier.py', 'w') as f:
    f.write(content)
