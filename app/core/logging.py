import logging
import json
import re
from datetime import datetime
from typing import Any, Dict
from app.core.enums import LogLevel, EventCategory
from app.core.paths import PATHS
from app.core.run_context import get_active_context

# Sensitive keys that should trigger redaction
SENSITIVE_KEYS = {
    "api_key",
    "api_secret",
    "secret_key",
    "telegram_token",
    "bot_token",
    "chat_id",
    "password",
    "token",
    "secret",
    "private_key",
}


def redact_secrets(data: str) -> str:
    """Masks secret values in a JSON-like string."""
    try:
        # Simple attempt to parse and redact if it's JSON
        parsed = json.loads(data)
        if isinstance(parsed, dict):
            _redact_dict(parsed)
            return json.dumps(parsed)
    except Exception:
        pass

    # Regex fallback for key=value or "key": "value" patterns
    redacted_data = data
    for key in SENSITIVE_KEYS:
        # Matches "key": "value" or 'key': 'value'
        pattern_json = rf'("{key}"|\'{key}\')\s*:\s*("[^"]+"|\'[^\']+\')'
        redacted_data = re.sub(
            pattern_json, r'\1: "***REDACTED***"', redacted_data, flags=re.IGNORECASE
        )

        # Matches key=value
        pattern_eq = rf"({key})\s*=\s*([^,\s]+)"
        redacted_data = re.sub(
            pattern_eq, r"\1=***REDACTED***", redacted_data, flags=re.IGNORECASE
        )

    return redacted_data


def _redact_dict(d: Dict[str, Any]) -> None:
    for k, v in d.items():
        if isinstance(v, dict):
            _redact_dict(v)
        elif isinstance(v, str) and any(sk in k.lower() for sk in SENSITIVE_KEYS):
            d[k] = "***REDACTED***"


from app.observability.telemetry import ingester
from app.observability.enums import ComponentType, AlertSeverity


def emit_telemetry(
    event_type: str,
    component: ComponentType,
    details: dict = None,
    severity: AlertSeverity = AlertSeverity.INFO,
):
    ctx = get_active_context()
    run_id = ctx.run_id if ctx else None
    ingester.capture_event(event_type, component, details, severity, run_id)


class StructuredJSONFormatter(logging.Formatter):

    def format(self, record: logging.LogRecord) -> str:
        ctx = get_active_context()
        log_obj = {
            "timestamp": datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "module": record.module,
            "message": record.getMessage(),
        }

        if ctx:
            log_obj["run_id"] = ctx.run_id
            log_obj["profile"] = ctx.profile.value

        if hasattr(record, "event_category"):
            log_obj["event"] = record.event_category

        if hasattr(record, "extra_data"):
            log_obj["extra"] = record.extra_data

        if record.exc_info:
            log_obj["exception"] = self.formatException(record.exc_info)

        json_str = json.dumps(log_obj)
        return redact_secrets(json_str)


class ConsoleFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        msg = super().format(record)
        return redact_secrets(msg)


def setup_logging(level: LogLevel = LogLevel.INFO) -> None:
    logger = logging.getLogger()

    # Clear existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(level.value)

    # File Handler (JSON)
    PATHS.logs.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(PATHS.logs / "app.log")
    file_handler.setFormatter(StructuredJSONFormatter())
    logger.addHandler(file_handler)

    # Console Handler (Human readable but redacted)
    console_handler = logging.StreamHandler()
    console_format = "%(asctime)s - %(levelname)s - [%(module)s] - %(message)s"
    console_handler.setFormatter(ConsoleFormatter(console_format))
    logger.addHandler(console_handler)


def get_logger(name: str):
    return logging.getLogger(name)
