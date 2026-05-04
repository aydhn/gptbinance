def test_spot_book_loading():
    from app.crossbook.books import SpotBook

    sb = SpotBook()
    sb.load_snapshot(
        [{"asset": "BTC", "free": 1.0, "locked": 0.5, "notional": 50000.0}]
    )
    assert len(sb.positions) == 1
    assert sb.positions[0].quantity == 1.5


def test_margin_book_loading():
    from app.crossbook.books import MarginBook

    mb = MarginBook()
    mb.load_snapshot(
        [{"asset": "ETH", "netAsset": -10.0, "borrowed": 10.0, "notional": -20000.0}]
    )
    assert len(mb.positions) == 1
    assert mb.positions[0].is_borrowed is True


def test_futures_book_loading():
    from app.crossbook.books import FuturesBook

    fb = FuturesBook()
    fb.load_snapshot([{"symbol": "BTCUSDT", "positionAmt": -1.5, "notional": -75000.0}])
    assert len(fb.positions) == 1
    assert fb.positions[0].asset == "BTC"
