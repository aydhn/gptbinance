import pytest
from app.core.enums import EnvironmentProfile
from app.connectors.binance.profile_resolver import ProfileResolver
from app.connectors.binance.enums import ConnectorMode


def test_resolve_mode():
    assert (
        ProfileResolver.resolve_mode(EnvironmentProfile.DEV)
        == ConnectorMode.PUBLIC_ONLY
    )
    assert (
        ProfileResolver.resolve_mode(EnvironmentProfile.PAPER)
        == ConnectorMode.PAPER_TRADING
    )
    assert (
        ProfileResolver.resolve_mode(EnvironmentProfile.TESTNET)
        == ConnectorMode.PAPER_TRADING
    )
    assert (
        ProfileResolver.resolve_mode(EnvironmentProfile.LIVE)
        == ConnectorMode.PUBLIC_ONLY
    )


def test_resolve_capabilities_dev():
    caps = ProfileResolver.resolve_capabilities(EnvironmentProfile.DEV)
    assert caps.can_read_public_market_data is True
    assert caps.can_place_orders is False
    assert caps.requires_real_keys is False
    assert caps.requires_internal_paper_engine is False


def test_resolve_capabilities_paper():
    caps = ProfileResolver.resolve_capabilities(EnvironmentProfile.PAPER)
    assert caps.requires_internal_paper_engine is True
    assert caps.can_place_orders is False


def test_resolve_capabilities_testnet():
    caps = ProfileResolver.resolve_capabilities(EnvironmentProfile.TESTNET)
    assert caps.requires_real_keys is True
    assert caps.supports_native_execution is True


def test_resolve_capabilities_live():
    caps = ProfileResolver.resolve_capabilities(EnvironmentProfile.LIVE)
    assert caps.requires_real_keys is True
    assert caps.can_place_orders is False  # Explicitly false for Phase 03


def test_get_base_url():
    # Dev uses mainnet
    assert (
        ProfileResolver.get_base_url(EnvironmentProfile.DEV)
        == "https://api.binance.com"
    )
    # Testnet uses testnet
    assert (
        ProfileResolver.get_base_url(EnvironmentProfile.TESTNET)
        == "https://testnet.binance.vision"
    )
    # Live uses mainnet
    assert (
        ProfileResolver.get_base_url(EnvironmentProfile.LIVE)
        == "https://api.binance.com"
    )
    # Override
    assert (
        ProfileResolver.get_base_url(EnvironmentProfile.DEV, use_testnet_config=True)
        == "https://testnet.binance.vision"
    )
