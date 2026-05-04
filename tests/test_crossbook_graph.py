from app.crossbook.graph import ExposureGraphBuilder

def test_exposure_graph_builder():
    builder = ExposureGraphBuilder()
    graph = builder.build_graph([], [])
    assert graph.nodes == []
    assert graph.edges == []
