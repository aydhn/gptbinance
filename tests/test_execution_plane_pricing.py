from app.execution_plane.pricing import ReferencePriceEngine


def test_pricing():
    data = {"best_bid": 100.0, "best_ask": 102.0}
    ref = ReferencePriceEngine.get_reference_price(data, "passive")
    assert ref == 101.0

    data2 = {"last_price": 50.0}
    ref2 = ReferencePriceEngine.get_reference_price(data2, "passive")
    assert ref2 == 50.0
