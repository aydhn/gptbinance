from app.market_truth.sources import (
    BinanceOfficialRestAdapter,
    BinanceOfficialWebsocketAdapter,
)


def test_rest_adapter_no_scraping():
    adapter = BinanceOfficialRestAdapter()
    res = adapter.fetch_snapshot()
    assert res["source"] == "official_rest"


def test_ws_adapter():
    adapter = BinanceOfficialWebsocketAdapter()
    res = adapter.fetch_snapshot()
    assert res["source"] == "official_ws"
