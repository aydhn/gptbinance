from dataclasses import dataclass
from app.core.enums import EnvironmentProfile
from app.connectors.binance.enums import ConnectorMode


@dataclass
class ConnectorCapabilities:
    can_read_public_market_data: bool
    can_read_exchange_metadata: bool
    can_place_orders: bool
    can_open_user_stream: bool
    requires_real_keys: bool
    supports_native_execution: bool
    requires_internal_paper_engine: bool


class ProfileResolver:
    """
    Resolves the active EnvironmentProfile into Binance connector behaviors and capabilities.
    """

    @staticmethod
    def resolve_mode(profile: EnvironmentProfile) -> ConnectorMode:
        """Determines the appropriate connector mode based on the environment profile."""
        if profile == EnvironmentProfile.DEV:
            return ConnectorMode.PUBLIC_ONLY
        elif profile == EnvironmentProfile.PAPER:
            return ConnectorMode.PAPER_TRADING
        elif profile == EnvironmentProfile.TESTNET:
            return (
                ConnectorMode.PAPER_TRADING
            )  # Treat testnet as paper for now, can be updated later
        elif profile == EnvironmentProfile.LIVE:
            # Enforce read-only / public only for this phase even in LIVE
            return ConnectorMode.PUBLIC_ONLY
        else:
            return ConnectorMode.DISABLED

    @staticmethod
    def resolve_capabilities(profile: EnvironmentProfile) -> ConnectorCapabilities:
        """Determines what the connector is allowed to do in the given profile."""

        # Base capabilities for all valid profiles in this phase (Phase 03)
        base_caps = ConnectorCapabilities(
            can_read_public_market_data=True,
            can_read_exchange_metadata=True,
            can_place_orders=False,  # Strictly disabled in Phase 03
            can_open_user_stream=False,  # Disabled in Phase 03
            requires_real_keys=False,
            supports_native_execution=False,
            requires_internal_paper_engine=False,
        )

        if profile == EnvironmentProfile.DEV:
            # Dev uses public data, no real keys needed
            return base_caps
        elif profile == EnvironmentProfile.PAPER:
            base_caps.requires_internal_paper_engine = True
            return base_caps
        elif profile == EnvironmentProfile.TESTNET:
            # Testnet might use real keys for the testnet environment
            base_caps.requires_real_keys = True
            base_caps.supports_native_execution = True  # Even if order placement is false now, testnet supports it natively
            return base_caps
        elif profile == EnvironmentProfile.LIVE:
            # Live needs real keys (though not strictly for public data)
            base_caps.requires_real_keys = True
            base_caps.supports_native_execution = True
            return base_caps

        # Default fallback (disabled/unknown)
        return ConnectorCapabilities(False, False, False, False, False, False, False)

    @staticmethod
    def get_base_url(
        profile: EnvironmentProfile, use_testnet_config: bool = False
    ) -> str:
        """Returns the appropriate Binance API base URL."""

        # If testnet is explicitly requested or profile is testnet
        if profile == EnvironmentProfile.TESTNET or use_testnet_config:
            return "https://testnet.binance.vision"

        # Default to mainnet for Dev, Paper, Live
        return "https://api.binance.com"
