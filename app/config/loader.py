import os
import json
from typing import Dict, Any
from app.config.models import AppConfig
from app.core.enums import EnvironmentProfile
from pydantic import SecretStr

def _load_env_to_dict() -> Dict[str, Any]:
    """Basic extraction of env vars into nested dict structure for Pydantic."""
    config_dict: Dict[str, Any] = {
        "general": {}, "logging": {}, "storage": {},
        "telegram": {}, "binance": {}, "execution": {},
        "risk": {}, "live_guard": {}
    }

    # Mapping env vars to nested structure
    env_map = {
        "PROFILE": ("general", "profile"),
        "LOG_LEVEL": ("logging", "level"),
        "TELEGRAM_ENABLED": ("telegram", "enabled"),
        "TELEGRAM_BOT_TOKEN": ("telegram", "bot_token"),
        "TELEGRAM_CHAT_ID": ("telegram", "chat_id"),
        "BINANCE_API_KEY": ("binance", "api_key"),
        "BINANCE_API_SECRET": ("binance", "api_secret"),
        "BINANCE_USE_TESTNET": ("binance", "use_testnet"),
        "EXECUTION_ENABLED": ("execution", "enabled"),
        "RISK_HARD_STOPS": ("risk", "hard_stops_enabled"),
        "LIVE_CONFIRMATION": ("live_guard", "live_confirmation"),
    }

    for env_var, (section, key) in env_map.items():
        val = os.getenv(env_var)
        if val is not None:
            # Handle booleans
            if val.lower() in ("true", "1", "yes"):
                val = True
            elif val.lower() in ("false", "0", "no"):
                val = False
            config_dict[section][key] = val

    return config_dict

def load_config() -> AppConfig:
    """Loads configuration prioritizing Environment Variables -> Defaults."""
    raw_dict = _load_env_to_dict()
    return AppConfig(**raw_dict)

def get_effective_config_dict(config: AppConfig, mask_secrets: bool = True) -> Dict[str, Any]:
    """Returns the effective config as a dictionary, masking secrets if requested."""
    dump = config.model_dump()

    if mask_secrets:
        # Pydantic's SecretStr already obfuscates in model_dump() usually,
        # but let's be explicit and ensure we stringify it securely.
        dump_json = config.model_dump_json()
        import app.core.logging as app_logging
        redacted_json = app_logging.redact_secrets(dump_json)
        return json.loads(redacted_json)

    return dump
