import pytest
from unittest.mock import MagicMock
from app.connectors.binance.exchange_info_service import ExchangeInfoService
from app.connectors.binance.enums import SymbolStatus, MarketType


def test_parse_exchange_info_success():
    mock_client = MagicMock()
    mock_data = {
        "serverTime": 123456789,
        "rateLimits": [
            {
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
            }
        ],
        "symbols": [
            {
                "symbol": "BTCUSDT",
                "status": "TRADING",
                "baseAsset": "BTC",
                "quoteAsset": "USDT",
                "permissions": ["SPOT", "MARGIN"],
                "baseAssetPrecision": 8,
                "quoteAssetPrecision": 8,
                "filters": [{"filterType": "PRICE_FILTER", "tickSize": "0.01"}],
            },
            {
                "symbol": "ETHUSDT",
                "status": "BREAK",
                "baseAsset": "ETH",
                "quoteAsset": "USDT",
                "permissions": ["MARGIN"],
                "filters": [],
            },
        ],
    }

    mock_client.get.return_value = mock_data
    service = ExchangeInfoService(mock_client)

    snapshot = service.get_exchange_info()

    assert snapshot.server_time == 123456789
    assert len(snapshot.rate_limits) == 1
    assert snapshot.rate_limits[0].limit == 1200

    assert len(snapshot.symbols) == 2

    btc = snapshot.symbols[0]
    assert btc.symbol == "BTCUSDT"
    assert btc.status == SymbolStatus.TRADING
    assert btc.is_spot_trading_allowed is True
    assert btc.is_margin_trading_allowed is True
    assert len(btc.filters) == 1
    assert (
        getattr(btc.filters[0], "__pydantic_extra__", btc.filters[0].__dict__).get(
            "tickSize"
        )
        == "0.01"
    )

    eth = snapshot.symbols[1]
    assert eth.symbol == "ETHUSDT"
    assert eth.status == SymbolStatus.BREAK
    assert eth.is_spot_trading_allowed is False  # SPOT not in permissions
    assert eth.is_tradable is False


def test_parse_exchange_info_unknown_status():
    mock_client = MagicMock()
    mock_data = {
        "symbols": [
            {
                "symbol": "NEWCOIN",
                "status": "WEIRD_NEW_STATUS",
                "baseAsset": "NEW",
                "quoteAsset": "USDT",
                "permissions": ["SPOT"],
            }
        ]
    }

    mock_client.get.return_value = mock_data
    service = ExchangeInfoService(mock_client)

    snapshot = service.get_exchange_info()
    assert len(snapshot.symbols) == 1
    # Should fallback to UNKNOWN rather than crashing
    assert snapshot.symbols[0].status == SymbolStatus.UNKNOWN
