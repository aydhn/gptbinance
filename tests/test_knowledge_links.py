import pytest
from app.knowledge.models import KnowledgeLink
from app.knowledge.links import KnowledgeGraph


def test_knowledge_graph():
    graph = KnowledgeGraph()
    link = KnowledgeLink(source_id="A", target_id="B", link_type="relates_to")
    graph.add_link(link)

    outbound = graph.get_outbound_links("A")
    assert len(outbound) == 1
    assert outbound[0].target_id == "B"

    inbound = graph.get_inbound_links("B")
    assert len(inbound) == 1
    assert inbound[0].source_id == "A"
