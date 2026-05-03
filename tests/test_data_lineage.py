import pytest
from app.data_governance import LineageGraph, LineageNode, LineageEdgeType, DatasetRef, DatasetType, LineageIntegrityError

def test_lineage_graph_basic():
    graph = LineageGraph()
    ref1 = DatasetRef(dataset_id="d1", dataset_type=DatasetType.RAW_MARKET_DATA, version="v1")
    ref2 = DatasetRef(dataset_id="d2", dataset_type=DatasetType.NORMALIZED_DATA, version="v1")
    n1 = LineageNode(node_id="n1", dataset_ref=ref1, producing_module="sysA")
    n2 = LineageNode(node_id="n2", dataset_ref=ref2, producing_module="sysB")

    graph.add_node(n1)
    graph.add_node(n2)
    graph.add_edge("n1", "n2", LineageEdgeType.DERIVED_FROM)

    downstream = graph.get_downstream("n1")
    assert len(downstream) == 1
    assert downstream[0].node_id == "n2"

def test_lineage_graph_cycle_prevention():
    graph = LineageGraph()
    ref1 = DatasetRef(dataset_id="d1", dataset_type=DatasetType.RAW_MARKET_DATA, version="v1")
    n1 = LineageNode(node_id="n1", dataset_ref=ref1, producing_module="sysA")
    n2 = LineageNode(node_id="n2", dataset_ref=ref1, producing_module="sysB")

    graph.add_node(n1)
    graph.add_node(n2)
    graph.add_edge("n1", "n2", LineageEdgeType.DERIVED_FROM)

    with pytest.raises(LineageIntegrityError):
         graph.add_edge("n2", "n1", LineageEdgeType.DERIVED_FROM)
