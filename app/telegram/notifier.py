import logging
import requests
from typing import Optional

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
