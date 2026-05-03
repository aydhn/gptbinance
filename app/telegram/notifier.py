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

    def notify_replay_completed(
        self, run_id: str, severity: NotificationSeverity = NotificationSeverity.INFO
    ):
        logger.info(f"TELEGRAM [{severity.value.upper()}]: Replay {run_id} completed.")

    def notify_replay_mismatch(self, run_id: str):
        logger.warning(f"TELEGRAM [WARNING]: Replay mismatch detected in run {run_id}.")

    def notify_replayability_low(self, run_id: str):
        logger.warning(f"TELEGRAM [WARNING]: Replayability score low for run {run_id}.")

    def notify_forensic_bundle_ready(self, run_id: str):
        logger.info(f"TELEGRAM [INFO]: Forensic bundle ready for run {run_id}.")

    def notify_counterfactual_caution(self, run_id: str):
        logger.warning(
            f"TELEGRAM [WARNING]: Caution regarding counterfactual run {run_id}. Not historical reality."
        )

    def notify_stale_knowledge(self, item_id: str, severity: str, warnings: list):
        from app.telegram.templates import KnowledgeTemplates

        msg = KnowledgeTemplates.stale_runbook_warning(item_id, severity, warnings)
        print(f"[Telegram Mock] {msg}")

    def notify_lesson_adopted(self, item_id: str, title: str):
        from app.telegram.templates import KnowledgeTemplates

        msg = KnowledgeTemplates.lesson_adopted(item_id, title)
        print(f"[Telegram Mock] {msg}")

    def notify_readiness_expiring(self, operator_id: str, reasons: list):
        from app.telegram.templates import KnowledgeTemplates

        msg = KnowledgeTemplates.readiness_expiring(operator_id, reasons)
        print(f"[Telegram Mock] {msg}")

    def notify_knowledge_gap(self, action_type: str):
        from app.telegram.templates import KnowledgeTemplates

        msg = KnowledgeTemplates.knowledge_gap(action_type)
        print(f"[Telegram Mock] {msg}")


telegram_notifier = ReplayNotifier()
