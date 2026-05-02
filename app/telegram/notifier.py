
from .templates import *
import logging
import requests
from typing import Optional, Any

logger = logging.getLogger(__name__)


class BaseNotifier:
    def send_message(self, message: str) -> None:
        raise NotImplementedError

    def notify_stream_degraded(self, symbol: str, reason: str) -> None:
        msg = f"⚠️ STREAM DEGRADED: {symbol} - {reason}"
        self.send_message(msg)

    def notify_stream_reconnect_storm(self) -> None:
        msg = "🚨 RECONNECT STORM DETECTED: Stream health is failing rapidly."
        self.send_message(msg)

    def notify_live_start(self, run_id: str, config: str) -> None:
        pass

    def notify_cap_hit(self, run_id: str, cap_type: str, reason: str) -> None:
        pass

    def notify_flatten(
        self, run_id: str, success: bool, cancelled: int, closed: int
    ) -> None:
        pass

    def notify_rollback(self, run_id: str, severity: str, reason: str) -> None:
        pass

    def notify_portfolio_allocation(self, run_id: str, summary: Any) -> None:
        pass

    def notify_concentration_warning(
        self, run_id: str, severity: str, breaches: list
    ) -> None:
        pass

    def notify_capital_exhausted(self, run_id: str, available: float) -> None:
        pass


class NoOpNotifier(BaseNotifier):
    def send_message(self, message: str) -> None:
        logger.debug(f"NoOpNotifier simulated send: {message}")


class TelegramNotifier(BaseNotifier):
    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{self.token}/sendMessage"

    def send_message(self, message: str) -> None:
        try:
            payload = {"chat_id": self.chat_id, "text": message, "parse_mode": "HTML"}
            # Timeout is strictly enforced to prevent hanging the runtime
            response = requests.post(self.base_url, json=payload, timeout=2.0)
            if not response.ok:
                logger.error(
                    f"Telegram send failed: {response.status_code} - {response.text}",
                    extra={"event_category": "telegram_error"},
                )
            else:
                logger.debug("Telegram message sent successfully.")
        except Exception as e:
            logger.error(
                f"Telegram connection error: {e}",
                extra={"event_category": "telegram_error"},
            )

    def notify_portfolio_allocation(self, run_id: str, summary: Any) -> None:
        from app.telegram.templates import render_portfolio_summary

        msg = render_portfolio_summary(run_id, summary)
        self.send_message(msg)

    def notify_concentration_warning(
        self, run_id: str, severity: str, breaches: list
    ) -> None:
        from app.telegram.templates import render_concentration_warning

        msg = render_concentration_warning(run_id, severity, breaches)
        self.send_message(msg)

    def notify_capital_exhausted(self, run_id: str, available: float) -> None:
        from app.telegram.templates import render_capital_exhausted

        msg = render_capital_exhausted(run_id, available)
        self.send_message(msg)



    # Phase 22 Analytics Additions
    def notify_analytics_summary(self, summary_text: str) -> None:
        self.send_message(summary_text)

    def notify_execution_degraded(self, run_id: str, submit: int, rej: int) -> None:
        from app.telegram.templates import render_execution_quality_degraded
        self.send_message(render_execution_quality_degraded(run_id, submit, rej))

    def notify_divergence_warning(self, run_id: str, div_type: str, severity: str, evidence: str) -> None:
        from app.telegram.templates import render_divergence_warning
        self.send_message(render_divergence_warning(run_id, div_type, severity, evidence))

    def notify_anomaly_cluster(self, run_id: str, anomaly_type: str, evidence: str) -> None:
        from app.telegram.templates import render_anomaly_cluster
        self.send_message(render_anomaly_cluster(run_id, anomaly_type, evidence))

    def notify_strategy_decay(self, run_id: str, family: str, hit_rate: float) -> None:
        from app.telegram.templates import render_strategy_decay_warning
        self.send_message(render_strategy_decay_warning(run_id, family, hit_rate))

    def notify_root_cause(self, run_id: str, hypothesis_id: str, causes: list) -> None:
        from app.telegram.templates import render_root_cause_summary
        self.send_message(render_root_cause_summary(run_id, hypothesis_id, causes))

    def notify_health_degraded(self, component: str, severity: str, explanation: str) -> None:
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

def get_notifier(config) -> BaseNotifier:

    if (
        hasattr(config, "telegram")
        and config.telegram.enabled
        and config.telegram.bot_token
        and config.telegram.chat_id
    ):
        return TelegramNotifier(
            token=config.telegram.bot_token.get_secret_value(),
            chat_id=config.telegram.chat_id.get_secret_value(),
        )
    return NoOpNotifier()

    # Phase 21 Governance additions
    async def notify_governance_event(self, event_type: str, details: dict):
        # Mute logging or send actual TG msg
        print(f"TELEGRAM GOVERNANCE: {event_type} - {details}")

    def send_automation_alert(self, msg: str, severity: str = "warning"):
        self.send_message(f"[{severity.upper()}] {msg}")

    def notify_release_built(self, version: str) -> None:
        from app.telegram.templates import render_release_built
        self.send_message(render_release_built(version))

    def notify_host_probe_failed(self, version: str, errors: list) -> None:
        from app.telegram.templates import render_host_probe_failed
        self.send_message(render_host_probe_failed(version, errors))

    def notify_upgrade_blocked(self, version: str, reason: str) -> None:
        from app.telegram.templates import render_upgrade_blocked
        self.send_message(render_upgrade_blocked(version, reason))
