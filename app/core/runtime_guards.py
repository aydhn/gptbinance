import logging
from app.config.models import AppConfig
from app.core.enums import EnvironmentProfile

logger = logging.getLogger(__name__)

class LiveModeError(Exception):
    pass

def check_live_guard(config: AppConfig) -> None:
    """Strictly validates if the application is allowed to run in LIVE mode."""
    if config.general.profile != EnvironmentProfile.LIVE:
        return # Not live, no strict guards needed

    # 1. Profile MUST be explicitly live
    # (Checked implicitly above)

    # 2. Confirmation phrase MUST match exactly
    EXPECTED_CONFIRMATION = "I_UNDERSTAND_THE_RISKS_AND_ALLOW_LIVE_TRADING"
    if config.live_guard.live_confirmation != EXPECTED_CONFIRMATION:
        raise LiveModeError(
            "LIVE mode blocked: live_confirmation does not match expected phrase."
        )

    # 3. Execution MUST be logically enabled for LIVE to make sense
    if not config.execution.enabled:
        raise LiveModeError("LIVE mode blocked: Execution is disabled.")

    # 4. Mandatory secrets MUST be present
    if not config.binance.api_key or not config.binance.api_secret:
        raise LiveModeError("LIVE mode blocked: Missing Binance API credentials.")

    # 5. Must NOT be testnet
    if config.binance.use_testnet:
        raise LiveModeError("LIVE mode blocked: use_testnet is True.")

    # 6. Risk must be enabled
    if not config.risk.hard_stops_enabled:
        raise LiveModeError("LIVE mode blocked: Risk hard stops must be enabled.")

    logger.warning("LIVE GUARD PASSED: Application is operating with REAL FUNDS.")
