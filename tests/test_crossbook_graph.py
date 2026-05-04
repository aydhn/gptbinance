def test_exposure_graph_builder():
    from app.crossbook.graph import ExposureGraphBuilder
    from app.crossbook.mapping import PositionMapper
    from app.crossbook.models import BookPositionRef
    from app.crossbook.enums import BookType

    mapper = PositionMapper()
    builder = ExposureGraphBuilder(mapper)
    positions = [
        BookPositionRef(
            book_type=BookType.MARGIN,
            symbol="ETHUSDT",
            asset="ETH",
            quantity=1.0,
            notional=3000.0,
            is_borrowed=True,
        )
    ]
    graph = builder.build(positions)
    assert len(graph.nodes) == 1
    assert len(graph.edges) == 1
    assert graph.edges[0].edge_type == "BORROW_DEPENDENCY"
