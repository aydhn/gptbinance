from app.market_truth.symbol_health import SymbolHealthAggregator


def test_symbol_health():
    agg = SymbolHealthAggregator()
    res = agg.aggregate("BTC", [{"is_healthy": True}, {"is_healthy": True}])
    assert res.is_healthy is True
