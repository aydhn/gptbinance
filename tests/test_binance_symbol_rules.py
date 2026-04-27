import pytest
from decimal import Decimal
from app.connectors.binance.models import SymbolMetadata, SymbolFilter
from app.connectors.binance.enums import SymbolStatus, MarketType
from app.connectors.binance.symbol_rules import SymbolRules


@pytest.fixture
def dummy_symbol_meta():
    filters = [
        SymbolFilter(filterType="PRICE_FILTER", tickSize="0.01"),
        SymbolFilter(
            filterType="LOT_SIZE", stepSize="0.001", minQty="0.005", maxQty="1000"
        ),
        SymbolFilter(filterType="NOTIONAL", minNotional="10.0"),
    ]
    return SymbolMetadata(
        symbol="BTCUSDT",
        status=SymbolStatus.TRADING,
        base_asset="BTC",
        quote_asset="USDT",
        is_spot_trading_allowed=True,
        is_margin_trading_allowed=False,
        base_asset_precision=8,
        quote_asset_precision=8,
        base_commission_precision=8,
        quote_commission_precision=8,
        filters=filters,
    )


def test_round_price(dummy_symbol_meta):
    assert SymbolRules.round_price(100.005, dummy_symbol_meta) == Decimal("100.00")
    assert SymbolRules.round_price(100.019, dummy_symbol_meta) == Decimal("100.01")
    assert SymbolRules.round_price(100, dummy_symbol_meta) == Decimal("100")


def test_round_quantity(dummy_symbol_meta):
    assert SymbolRules.round_quantity(1.0019, dummy_symbol_meta) == Decimal("1.001")
    assert SymbolRules.round_quantity(1.5, dummy_symbol_meta) == Decimal("1.5")
    assert SymbolRules.round_quantity(0.0009, dummy_symbol_meta) == Decimal("0")


def test_check_min_notional(dummy_symbol_meta):
    # 10 * 1 = 10 (valid)
    assert SymbolRules.check_min_notional(10.0, 1.0, dummy_symbol_meta) is True
    # 9 * 1 = 9 (invalid, min is 10)
    assert SymbolRules.check_min_notional(9.0, 1.0, dummy_symbol_meta) is False


def test_is_valid_quantity(dummy_symbol_meta):
    # minQty is 0.005
    assert SymbolRules.is_valid_quantity(0.01, dummy_symbol_meta) is True
    assert SymbolRules.is_valid_quantity(0.004, dummy_symbol_meta) is False
    assert (
        SymbolRules.is_valid_quantity(1001, dummy_symbol_meta) is False
    )  # maxQty 1000
