import logging

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

    def send_message(self, message: str) -> None:
        # Skeleton for future implementation
        logger.info(
            f"Would send to Telegram: {message}", extra={"event_category": "telegram"}
        )
        pass


def get_notifier(config) -> BaseNotifier:
    if (
        config.telegram.enabled
        and config.telegram.bot_token
        and config.telegram.chat_id
    ):
        return TelegramNotifier(
            token=config.telegram.bot_token.get_secret_value(),
            chat_id=config.telegram.chat_id.get_secret_value(),
        )
    return NoOpNotifier()
