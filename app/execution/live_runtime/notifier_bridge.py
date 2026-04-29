from app.telegram.notifier import BaseNotifier
from app.execution.live_runtime.models import LiveSessionConfig
import time
import logging

logger = logging.getLogger(__name__)


class LiveNotifierBridge:
    def __init__(self, notifier: BaseNotifier):
        self.notifier = notifier
        self.last_sent: dict[str, float] = {}
        # Rate limit settings (seconds)
        self.limits = {
            "fill": 60,  # Max 1 fill notification per minute per symbol
            "cap_hit": 10,
            "error": 10,
        }

    def _can_send(self, key: str, limit_seconds: int) -> bool:
        now = time.time()
        if key not in self.last_sent:
            self.last_sent[key] = now
            return True
        if now - self.last_sent[key] >= limit_seconds:
            self.last_sent[key] = now
            return True
        return False

    def notify_live_start(self, run_id: str, config: LiveSessionConfig) -> None:
        try:
            # We assume render_live_start exists in templates
            from app.telegram.templates import render_live_start

            msg = render_live_start(run_id, config)
            self.notifier.send_message(msg)
        except Exception as e:
            logger.error(f"Failed to notify live start: {e}")

    def notify_live_fill(
        self, run_id: str, symbol: str, side: str, qty: float, price: float, pnl: float
    ) -> None:
        key = f"fill_{symbol}"
        if not self._can_send(key, self.limits["fill"]):
            return

        try:
            # Fallback to paper template if live not ready
            from app.telegram.templates import render_paper_fill_summary

            msg = render_paper_fill_summary(
                run_id, symbol, side, qty, price, pnl
            ).replace("Paper Fill", "LIVE Fill")
            self.notifier.send_message(msg)
        except Exception as e:
            logger.error(f"Failed to notify live fill: {e}")

    def notify_cap_hit(self, run_id: str, cap_type: str, reason: str) -> None:
        key = "cap_hit"
        if not self._can_send(key, self.limits["cap_hit"]):
            return

        try:
            from app.telegram.templates import render_live_cap_hit

            msg = render_live_cap_hit(run_id, cap_type, reason)
            self.notifier.send_message(msg)
        except Exception as e:
            logger.error(f"Failed to notify cap hit: {e}")

    def notify_flatten(
        self, run_id: str, success: bool, cancelled: int, closed: int
    ) -> None:
        try:
            from app.telegram.templates import render_live_flatten

            msg = render_live_flatten(run_id, success, cancelled, closed)
            self.notifier.send_message(msg)
        except Exception as e:
            logger.error(f"Failed to notify flatten: {e}")

    def notify_rollback(self, run_id: str, severity: str, reason: str) -> None:
        try:
            from app.telegram.templates import render_live_rollback

            msg = render_live_rollback(run_id, severity, reason)
            self.notifier.send_message(msg)
        except Exception as e:
            logger.error(f"Failed to notify rollback: {e}")
