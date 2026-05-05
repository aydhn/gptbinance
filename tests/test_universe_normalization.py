import pytest
from app.universe.normalization import BinanceMetadataNormalizer
from app.universe.enums import InstrumentType, InstrumentStatus


def test_normalize_spot_instrument():
    normalizer = BinanceMetadataNormalizer()
    raw_data = {
        "symbol": "BTCUSDT",
        "isSpotTradingAllowed": True,
        "status": "TRADING",
        "baseAsset": "BTC",
        "quoteAsset": "USDT",
        "filters": [
            {
                "filterType": "PRICE_FILTER",
                "tickSize": "0.01",
                "minPrice": "0.01",
                "maxPrice": "100000.0",
            },
            {
                "filterType": "LOT_SIZE",
                "stepSize": "0.00001",
                "minQty": "0.00001",
                "maxQty": "100.0",
            },
        ],
    }

    inst = normalizer.normalize(raw_data)

    assert inst.ref.symbol == "BTCUSDT"
    assert inst.ref.product_type == InstrumentType.SPOT
    assert inst.status == InstrumentStatus.TRADING
    assert inst.filters.tick_size is not None
    assert inst.filters.tick_size.tick_size == 0.01
    assert inst.filters.step_size is not None
    assert inst.filters.step_size.step_size == 0.00001
