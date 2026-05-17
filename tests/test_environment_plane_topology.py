import pytest
from app.environment_plane.topology import define_topology
from app.environment_plane.enums import TopologyClass

def test_define_topology():
    topology = define_topology(TopologyClass.SHADOW, "Shadow topology for isolation")
    assert topology.topology_class == TopologyClass.SHADOW
    assert topology.proof_notes == "Shadow topology for isolation"
