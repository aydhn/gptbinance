def test_netting_evaluator():
    from app.crossbook.netting import NetExposureEvaluator
    from app.crossbook.graph import ExposureGraphBuilder
    from app.crossbook.mapping import PositionMapper
    from app.crossbook.models import BookPositionRef
    from app.crossbook.enums import BookType, ExposureClass

    mapper = PositionMapper()
    builder = ExposureGraphBuilder(mapper)
    evaluator = NetExposureEvaluator()

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
    graph = builder.build(positions)
    snapshot = evaluator.evaluate(graph)

    assert "BTC" in snapshot.assets
    btc_exp = snapshot.assets["BTC"]
    assert btc_exp.directional.net_notional == 0.0
    assert btc_exp.exposure_class == ExposureClass.NEUTRAL_HEDGED
