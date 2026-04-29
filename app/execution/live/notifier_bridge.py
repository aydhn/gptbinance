import logging
from typing import Dict, Any
from app.execution.live.enums import SafetyGateSeverity

logger = logging.getLogger(__name__)


class ExecutionNotifierBridge:
    def __init__(self, telegram_bot: Any = None):
        self.telegram_bot = telegram_bot

    async def notify_gate_block(
        self, reason: str, severity: str = SafetyGateSeverity.BLOCK.value
    ):
        msg = f"🛡️ [GATE BLOCK] {reason}"
        logger.warning(msg)
        if self.telegram_bot and severity == SafetyGateSeverity.BLOCK.value:
            try:
                await self.telegram_bot.send_message(msg)
            except Exception as e:
                logger.error(f"Notifier failed: {e}")

    async def notify_order_reject(self, client_order_id: str, reason: str):
        msg = f"❌ [ORDER REJECT] {client_order_id}: {reason}"
        logger.error(msg)
        if self.telegram_bot:
            try:
                await self.telegram_bot.send_message(msg)
            except Exception:
                pass

    async def notify_reconciliation_drift(self, details: str):
        msg = f"⚠️ [RECONCILIATION DRIFT] {details}"
        logger.warning(msg)
        if self.telegram_bot:
            try:
                await self.telegram_bot.send_message(msg)
            except Exception:
                pass
