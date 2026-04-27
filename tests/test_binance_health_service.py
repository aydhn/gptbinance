import pytest
from unittest.mock import MagicMock, patch
from app.config.models import AppConfig
from app.core.enums import EnvironmentProfile
from app.connectors.binance.health_service import HealthService
from app.connectors.binance.models import ServerTimeSnapshot, ExchangeInfoSnapshot


@patch("app.connectors.binance.health_service.ClientFactory.create_public_client")
@patch("app.connectors.binance.health_service.TimeService")
@patch("app.connectors.binance.health_service.ExchangeInfoService")
def test_check_health_all_good(mock_exchange, mock_time, mock_factory):
    config = AppConfig()

    mock_client = MagicMock()
    mock_factory.return_value = mock_client

    mock_time_instance = MagicMock()
    # Good latency
    mock_time_instance.get_server_time.return_value = ServerTimeSnapshot(
        server_time=1000, local_time=1100, latency_ms=100, drift_ms=0
    )
    mock_time.return_value = mock_time_instance

    mock_exchange_instance = MagicMock()
    mock_exchange_instance.get_exchange_info.return_value = ExchangeInfoSnapshot(
        server_time=1000,
        rate_limits=[],
        symbols=[
            {
                "symbol": "BTCUSDT",
                "status": "TRADING",
                "base_asset": "BTC",
                "quote_asset": "USDT",
                "is_spot_trading_allowed": True,
                "is_margin_trading_allowed": False,
                "base_asset_precision": 8,
                "quote_asset_precision": 8,
                "base_commission_precision": 8,
                "quote_commission_precision": 8,
            }
        ],
    )
    mock_exchange.return_value = mock_exchange_instance

    service = HealthService(config, EnvironmentProfile.PAPER)
    result = service.check_health()

    assert result.config_ready is True
    assert result.client_created is True
    assert result.server_time_ok is True
    assert result.exchange_info_ok is True
    assert result.latency_status == "GOOD"
    assert result.overall_status == "HEALTHY"
    assert result.is_healthy is True
    assert len(result.errors) == 0


@patch("app.connectors.binance.health_service.ClientFactory.create_public_client")
@patch("app.connectors.binance.health_service.TimeService")
@patch("app.connectors.binance.health_service.ExchangeInfoService")
def test_check_health_poor_latency(mock_exchange, mock_time, mock_factory):
    config = AppConfig()

    mock_client = MagicMock()
    mock_factory.return_value = mock_client

    mock_time_instance = MagicMock()
    # Poor latency
    mock_time_instance.get_server_time.return_value = ServerTimeSnapshot(
        server_time=1000, local_time=3500, latency_ms=2500, drift_ms=0
    )
    mock_time.return_value = mock_time_instance

    mock_exchange_instance = MagicMock()
    mock_exchange_instance.get_exchange_info.return_value = ExchangeInfoSnapshot(
        server_time=1000,
        rate_limits=[],
        symbols=[
            {
                "symbol": "BTCUSDT",
                "status": "TRADING",
                "base_asset": "BTC",
                "quote_asset": "USDT",
                "is_spot_trading_allowed": True,
                "is_margin_trading_allowed": False,
                "base_asset_precision": 8,
                "quote_asset_precision": 8,
                "base_commission_precision": 8,
                "quote_commission_precision": 8,
            }
        ],
    )
    mock_exchange.return_value = mock_exchange_instance

    service = HealthService(config, EnvironmentProfile.PAPER)
    result = service.check_health()

    assert result.server_time_ok is True
    assert result.latency_status == "POOR"
    assert result.overall_status == "DEGRADED"
    assert result.is_healthy is True  # Still true, but degraded
    assert len(result.errors) == 1
    assert "High latency" in result.errors[0]


@patch("app.connectors.binance.health_service.ClientFactory.create_public_client")
def test_check_health_client_failure(mock_factory):
    config = AppConfig()
    mock_factory.side_effect = Exception("Network blocked")

    service = HealthService(config, EnvironmentProfile.PAPER)
    result = service.check_health()

    assert result.config_ready is True
    assert result.client_created is False
    assert result.overall_status == "FAILED"
    assert result.is_healthy is False
    assert "Failed to create client" in result.errors[0]
