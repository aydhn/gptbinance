import logging
from app.config.models import AppConfig
from app.core.enums import EnvironmentProfile

logger = logging.getLogger(__name__)

class ConfigurationError(Exception):
    pass

def validate_config_for_profile(config: AppConfig) -> None:
    """Validates the configuration based on the active profile."""
    profile = config.general.profile

    if profile == EnvironmentProfile.DEV:
        # Dev is permissive
        if config.execution.enabled:
            logger.warning("Execution is enabled in DEV mode. Use with caution.")

    elif profile == EnvironmentProfile.PAPER:
        # Paper should not need real API secrets, but might need testnet
        if not config.binance.use_testnet:
            logger.warning("Paper trading using real Binance endpoints. Ensure execution is disabled.")

    elif profile == EnvironmentProfile.TESTNET:
        # Testnet needs testnet enabled
        if not config.binance.use_testnet:
            raise ConfigurationError("TESTNET profile requires use_testnet=True")
        if not config.binance.api_key or not config.binance.api_secret:
            raise ConfigurationError("TESTNET profile requires Binance API credentials")

    elif profile == EnvironmentProfile.LIVE:
        # Live is strictly validated by runtime_guards.py, but basic checks here
        if config.binance.use_testnet:
            raise ConfigurationError("LIVE profile cannot use testnet endpoints")
        if not config.binance.api_key or not config.binance.api_secret:
            raise ConfigurationError("LIVE profile requires Binance API credentials")

    # General validations
    if config.telegram.enabled:
        if not config.telegram.bot_token or not config.telegram.chat_id:
            raise ConfigurationError("Telegram enabled but token/chat_id missing")
