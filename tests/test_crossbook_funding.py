def test_funding_analyzer():
    from app.crossbook.funding import FundingAnalyzer
    from app.crossbook.graph import ExposureGraphBuilder
    from app.crossbook.mapping import PositionMapper
    from app.crossbook.models import BookPositionRef
    from app.crossbook.enums import BookType, FundingBurdenClass

    mapper = PositionMapper()
    builder = ExposureGraphBuilder(mapper)
    analyzer = FundingAnalyzer()

    positions = [
        BookPositionRef(
            book_type=BookType.FUTURES,
            symbol="BTCUSDT",
            asset="BTC",
            quantity=-10.0,
            notional=-6000000.0,
        )
    ]
    graph = builder.build(positions)
    report = analyzer.analyze(graph)

    assert report.total_expected_drag > 500.0
    assert report.burden_class == FundingBurdenClass.SEVERE
