from app.market_truth.ordering import OrderingEngine
from app.market_truth.enums import OrderingSeverity


def test_ordering():
    engine = OrderingEngine()
    events = [{"id": 1}, {"id": 3}, {"id": 2}, {"id": -5}]
    res = engine.evaluate_ordering(events)
    assert len(res) == 2
    assert res[0].severity == OrderingSeverity.SLIGHTLY_LATE
    assert res[1].severity == OrderingSeverity.SEVERE_OUT_OF_ORDER
