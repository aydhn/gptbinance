def test_borrow_analyzer():
    from app.crossbook.borrow import BorrowAnalyzer
    from app.crossbook.graph import ExposureGraphBuilder
    from app.crossbook.mapping import PositionMapper
    from app.crossbook.models import BookPositionRef
    from app.crossbook.enums import BookType, BorrowDependencyClass

    mapper = PositionMapper()
    builder = ExposureGraphBuilder(mapper)
    analyzer = BorrowAnalyzer()

    positions = [
        BookPositionRef(
            book_type=BookType.MARGIN,
            symbol="USDT",
            asset="USDT",
            quantity=-60000.0,
            notional=-60000.0,
            is_borrowed=True,
        )
    ]
    graph = builder.build(positions)
    report = analyzer.analyze(graph)

    assert report.total_borrow_value == 60000.0
    assert report.dependency_class == BorrowDependencyClass.HIGH
