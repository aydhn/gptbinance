from app.market_truth.convergence import WebsocketRestConvergenceEngine
from app.market_truth.enums import ConvergenceVerdict


def test_convergence():
    engine = WebsocketRestConvergenceEngine()
    res = engine.check_convergence({"symbol": "BTC", "price": 100}, {"price": 100})
    assert res.verdict == ConvergenceVerdict.ALIGNED

    res_div = engine.check_convergence({"symbol": "BTC", "price": 100}, {"price": 105})
    assert res_div.verdict == ConvergenceVerdict.TRANSIENT_DIVERGENCE
