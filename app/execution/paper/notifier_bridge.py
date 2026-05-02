"""Bridge connecting paper runtime to telegram notifier."""

import logging
from typing import Any, Optional
from datetime import datetime, timedelta

from app.telegram.notifier import BaseNotifier
from app.telegram.templates import (
    render_session_started,
    render_session_stopped,
    render_risk_veto_storm,
    render_kill_switch_active,
    render_stream_degraded,
    render_paper_fill_summary,
    render_pnl_milestone,
    render_drawdown_warning,
)

logger = logging.getLogger(__name__)


class PaperNotifierBridge:
    def __init__(self, notifier: BaseNotifier):
        self.notifier = notifier
        self._last_veto_alert: Optional[datetime] = None
        self._last_degraded_alert: Optional[datetime] = None
        self._last_drawdown_alert: Optional[datetime] = None

        # Rate limit intervals
        self.veto_interval = timedelta(minutes=5)
        self.degraded_interval = timedelta(minutes=5)
        self.drawdown_interval = timedelta(minutes=15)

    def _should_send(self, last_sent: Optional[datetime], interval: timedelta) -> bool:
        now = datetime.utcnow()
        if last_sent is None or (now - last_sent) > interval:
            return True
        return False

    def notify_session_started(self, run_id: str, config: Any):
        msg = render_session_started(run_id, config)
        self.notifier.send_message(msg)

    def notify_session_stopped(self, run_id: str, reason: str, summary: Any):
        msg = render_session_stopped(run_id, reason, summary)
        self.notifier.send_message(msg)

    def notify_risk_veto_storm(self, run_id: str, symbol: str, count: int):
        if self._should_send(self._last_veto_alert, self.veto_interval):
            msg = render_risk_veto_storm(run_id, symbol, count)
            self.notifier.send_message(msg)
            self._last_veto_alert = datetime.utcnow()

    def notify_kill_switch(self, run_id: str, reason: str):
        # Kill switch is critical, bypass rate limiting
        msg = render_kill_switch_active(run_id, reason)
        self.notifier.send_message(msg)

    def notify_stream_degraded(self, run_id: str, symbol: str, lag_ms: float):
        if self._should_send(self._last_degraded_alert, self.degraded_interval):
            msg = render_stream_degraded(run_id, symbol, lag_ms)
            self.notifier.send_message(msg)
            self._last_degraded_alert = datetime.utcnow()

    def notify_fill(
        self, run_id: str, symbol: str, side: str, qty: float, price: float, pnl: float
    ):
        # Could spam if trading frequently. In a real system, might aggregate.
        msg = render_paper_fill_summary(run_id, symbol, side, qty, price, pnl)
        self.notifier.send_message(msg)

    def notify_pnl_milestone(self, run_id: str, pnl: float, equity: float):
        msg = render_pnl_milestone(run_id, pnl, equity)
        self.notifier.send_message(msg)

    def notify_drawdown_warning(self, run_id: str, drawdown: float):
        if self._should_send(self._last_drawdown_alert, self.drawdown_interval):
            msg = render_drawdown_warning(run_id, drawdown)
            self.notifier.send_message(msg)
            self._last_drawdown_alert = datetime.utcnow()
