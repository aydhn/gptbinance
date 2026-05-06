from app.postmortems.causal_graph import CausalGraphBuilder


def test_causal_graph_builder():
    builder = CausalGraphBuilder()
    graph = builder.build({}, {})
    assert len(graph.nodes) == 0
