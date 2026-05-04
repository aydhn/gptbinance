def test_position_mapper():
    from app.crossbook.mapping import PositionMapper
    from app.crossbook.models import BookPositionRef
    from app.crossbook.enums import BookType

    mapper = PositionMapper()
    positions = [
        BookPositionRef(
            book_type=BookType.SPOT,
            symbol="BTC",
            asset="BTC",
            quantity=1.0,
            notional=50000.0,
        ),
        BookPositionRef(
            book_type=BookType.FUTURES,
            symbol="BTCUSDT",
            asset="BTC",
            quantity=-1.0,
            notional=-50000.0,
        ),
    ]
    nodes = mapper.map_to_nodes(positions)
    assert len(nodes) == 1
    assert "BTC" in nodes
    assert len(nodes["BTC"].positions) == 2
    assert nodes["BTC"].total_quantity == 0.0
    assert nodes["BTC"].total_notional == 0.0
