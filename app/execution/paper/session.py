"""Paper session lifecycle management."""
import logging
import uuid
import time
from datetime import datetime, timedelta
from typing import Optional

from .models import (
    PaperSessionConfig,
    PaperSessionStatus,
    SessionStopReason,
    PaperSessionState,
    PaperRuntimeSummary,
    PaperArtifactManifest,
)
from .runtime import PaperRuntimeOrchestrator
from .notifier_bridge import PaperNotifierBridge
from .storage import PaperStorage
from app.telegram.notifier import get_notifier

logger = logging.getLogger(__name__)


class PaperSession:
    def __init__(self, config: PaperSessionConfig, base_config):
        self.run_id = f"paper_{uuid.uuid4().hex[:8]}"
        self.config = config
        self.base_config = base_config

        self.state = PaperSessionState(
            run_id=self.run_id,
            status=PaperSessionStatus.INITIALIZED,
            config=config,
            active_symbols=config.symbols,
        )

        # Use existing notifier if configured, else fallback
        if config.enable_telegram:
            self.notifier = get_notifier(base_config)
        else:
            from app.telegram.notifier import NoOpNotifier

            self.notifier = NoOpNotifier()

        self.notifier_bridge = PaperNotifierBridge(self.notifier)
        self.storage = PaperStorage()

        self.runtime = PaperRuntimeOrchestrator(
            run_id=self.run_id,
            config=self.config,
            notifier_bridge=self.notifier_bridge,
            storage=self.storage,
        )

    def start(self):
        logger.info(f"Starting paper session {self.run_id}")
        self.state.status = PaperSessionStatus.RUNNING
        self.state.start_time = datetime.utcnow()
        self.notifier_bridge.notify_session_started(self.run_id, self.config)

    def stop(self, reason: SessionStopReason = SessionStopReason.MANUAL):
        if self.state.status in [PaperSessionStatus.STOPPED, PaperSessionStatus.FAILED]:
            return

        logger.info(f"Stopping paper session {self.run_id} due to {reason}")
        self.state.status = PaperSessionStatus.STOPPING
        self.state.end_time = datetime.utcnow()

        summary = self._generate_summary(reason)
        manifest = PaperArtifactManifest(
            run_id=self.run_id, config=self.config, summary=summary
        )

        self.storage.save_manifest(manifest)
        self.notifier_bridge.notify_session_stopped(self.run_id, reason.value, summary)

        self.state.status = PaperSessionStatus.STOPPED

    def kill(self, reason: str):
        self.state.kill_switch_active = True
        self.notifier_bridge.notify_kill_switch(self.run_id, reason)
        self.stop(SessionStopReason.KILL_SWITCH)

    def _generate_summary(self, reason: SessionStopReason) -> PaperRuntimeSummary:
        return PaperRuntimeSummary(
            run_id=self.run_id,
            start_time=self.state.start_time,
            end_time=self.state.end_time,
            stop_reason=reason,
            total_orders=self.runtime.telemetry.orders_created,
            total_fills=self.runtime.telemetry.fills_executed,
            final_equity=self.runtime.pnl_tracker.current_equity,
            max_drawdown_pct=self.runtime.pnl_tracker.peak_equity
            - self.runtime.pnl_tracker.current_equity
            if self.runtime.pnl_tracker.peak_equity > 0
            else 0,  # Simple approx
            risk_veto_count=self.runtime.telemetry.risk_vetoes,
        )
