def test_conflict_detector():
    from app.crossbook.conflicts import ConflictDetector
    from app.crossbook.netting import NetExposureEvaluator
    from app.crossbook.graph import ExposureGraphBuilder
    from app.crossbook.mapping import PositionMapper
    from app.crossbook.models import BookPositionRef
    from app.crossbook.enums import BookType, OverlayReasonType, ConflictSeverity

    mapper = PositionMapper()
    builder = ExposureGraphBuilder(mapper)
    evaluator = NetExposureEvaluator()
    detector = ConflictDetector()

    # Simulating fake hedge setup (not entirely neutral)
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
            quantity=-0.99,
            notional=-49500.0,
        ),
    ]
    graph = builder.build(positions)
    net_exp = evaluator.evaluate(graph)

    # Artificially adjusting the net exposure class for test logic mapping inside ConflictDetector
    from app.crossbook.enums import ExposureClass, HedgeQuality

    net_exp.assets["BTC"].exposure_class = ExposureClass.NEUTRAL_HEDGED
    net_exp.assets["BTC"].hedge_quality = HedgeQuality.POOR

    conflicts = detector.detect(graph, net_exp)
    assert len(conflicts) > 0
    fake_hedges = [
        c for c in conflicts if c.conflict_type == OverlayReasonType.FAKE_HEDGE_DETECTED
    ]
    assert len(fake_hedges) == 1
    assert fake_hedges[0].severity == ConflictSeverity.MEDIUM
