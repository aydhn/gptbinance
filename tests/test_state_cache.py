import pytest
from app.data.state_cache import StateCache
from app.data.live_stream_models import KlineUpdateEvent, TickerEvent


def get_dummy_kline(symbol="BTCUSDT", interval="1m") -> KlineUpdateEvent:
    return KlineUpdateEvent(
        event_time=123456789,
        symbol=symbol,
        interval=interval,
        open_time=123000000,
        close_time=123059999,
        open_price=50000.0,
        high_price=51000.0,
        low_price=49000.0,
        close_price=50500.0,
        volume=10.0,
        quote_asset_volume=505000.0,
        number_of_trades=100,
        is_closed=False,
    )


def get_dummy_ticker(symbol="BTCUSDT") -> TickerEvent:
    return TickerEvent(
        event_time=123456789,
        symbol=symbol,
        price_change=100.0,
        price_change_percent=2.0,
        weighted_avg_price=50250.0,
        last_price=50500.0,
        last_quantity=0.1,
        open_price=50000.0,
        high_price=51000.0,
        low_price=49000.0,
        volume=100.0,
        quote_volume=5025000.0,
        open_time=120000000,
        close_time=123456789,
        first_trade_id=1,
        last_trade_id=100,
        number_of_trades=100,
    )


def test_update_get_kline():
    cache = StateCache()
    kline = get_dummy_kline()
    cache.update_kline(kline)

    res = cache.get_latest_kline("BTCUSDT", "1m")
    assert res is not None
    assert res.close_price == 50500.0

    # Check non-existent
    assert cache.get_latest_kline("ETHUSDT", "1m") is None
    assert cache.get_latest_kline("BTCUSDT", "5m") is None


def test_update_get_ticker():
    cache = StateCache()
    ticker = get_dummy_ticker()
    cache.update_ticker(ticker)

    res = cache.get_latest_ticker("BTCUSDT")
    assert res is not None
    assert res.last_price == 50500.0


def test_snapshot():
    cache = StateCache()
    cache.update_kline(get_dummy_kline())
    cache.update_ticker(get_dummy_ticker())

    snap = cache.get_snapshot()
    assert "BTCUSDT" in snap["klines"]
    assert "1m" in snap["klines"]["BTCUSDT"]
    assert "BTCUSDT" in snap["tickers"]
