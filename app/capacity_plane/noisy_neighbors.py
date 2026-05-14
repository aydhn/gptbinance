from datetime import datetime, timezone
from typing import Dict, List
from app.capacity_plane.models import NoisyNeighborReport

_noisy_neighbors: Dict[str, NoisyNeighborReport] = {}


def report_noisy_neighbor(
    resource_id: str,
    interfering_workloads: List[str],
    impacted_workloads: List[str],
    burst_collisions: int,
) -> NoisyNeighborReport:
    rec = NoisyNeighborReport(
        resource_id=resource_id,
        interfering_workloads=interfering_workloads,
        impacted_workloads=impacted_workloads,
        burst_collisions=burst_collisions,
        timestamp=datetime.now(timezone.utc),
    )
    _noisy_neighbors[f"{resource_id}_{datetime.now(timezone.utc).timestamp()}"] = rec
    return rec


def list_noisy_neighbors() -> List[NoisyNeighborReport]:
    return list(_noisy_neighbors.values())
