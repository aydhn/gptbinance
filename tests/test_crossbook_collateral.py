def test_collateral_analyzer():
    from app.crossbook.collateral import CollateralAnalyzer
    from app.crossbook.graph import ExposureGraphBuilder
    from app.crossbook.mapping import PositionMapper
    from app.crossbook.models import BookPositionRef
    from app.crossbook.enums import BookType, MarginMode

    mapper = PositionMapper()
    builder = ExposureGraphBuilder(mapper)
    analyzer = CollateralAnalyzer()

    positions = [
        BookPositionRef(
            book_type=BookType.MARGIN,
            symbol="BTC",
            asset="BTC",
            quantity=1.0,
            notional=50000.0,
            margin_mode=MarginMode.CROSS,
        )
    ]
    graph = builder.build(positions)
    report = analyzer.analyze(graph)

    assert report.total_locked == 50000.0
    assert report.total_usable == 10000.0
    assert report.pressure_ratio > 0.8
