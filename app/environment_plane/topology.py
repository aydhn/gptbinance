from app.environment_plane.models import EnvironmentTopologyRecord
from app.environment_plane.enums import TopologyClass

def define_topology(topology_class: TopologyClass, proof_notes: str) -> EnvironmentTopologyRecord:
    return EnvironmentTopologyRecord(topology_class=topology_class, proof_notes=proof_notes)
