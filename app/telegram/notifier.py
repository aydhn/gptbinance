# Modifying to add replay notifications
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class NotificationSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"

class ReplayNotifier:
    def __init__(self):
        pass

    def notify_replay_completed(self, run_id: str, severity: NotificationSeverity = NotificationSeverity.INFO):
        logger.info(f"TELEGRAM [{severity.value.upper()}]: Replay {run_id} completed.")

    def notify_replay_mismatch(self, run_id: str):
        logger.warning(f"TELEGRAM [WARNING]: Replay mismatch detected in run {run_id}.")

    def notify_replayability_low(self, run_id: str):
        logger.warning(f"TELEGRAM [WARNING]: Replayability score low for run {run_id}.")

    def notify_forensic_bundle_ready(self, run_id: str):
         logger.info(f"TELEGRAM [INFO]: Forensic bundle ready for run {run_id}.")

    def notify_counterfactual_caution(self, run_id: str):
         logger.warning(f"TELEGRAM [WARNING]: Caution regarding counterfactual run {run_id}. Not historical reality.")

telegram_notifier = ReplayNotifier()
