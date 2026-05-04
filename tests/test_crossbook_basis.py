def test_basis_analyzer():
    from app.crossbook.basis import BasisAnalyzer
    from app.crossbook.graph import ExposureGraphBuilder
    from app.crossbook.mapping import PositionMapper
    from app.crossbook.models import BookPositionRef
    from app.crossbook.enums import BookType

    mapper = PositionMapper()
    builder = ExposureGraphBuilder(mapper)
    analyzer = BasisAnalyzer()

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
    reports = analyzer.analyze(graph)

    assert len(reports) == 1
    assert reports[0].asset == "BTC"
    assert reports[0].basis_spread == 0.001
