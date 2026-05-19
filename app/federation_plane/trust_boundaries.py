from typing import Dict, List, Optional
from app.federation_plane.models import TrustBoundaryRecord
from app.federation_plane.exceptions import InvalidBoundaryDefinition


class TrustBoundaryManager:
    def __init__(self):
        self._boundaries: Dict[str, TrustBoundaryRecord] = {}

    def register(self, record: TrustBoundaryRecord):
        if not record.boundary_id:
            raise InvalidBoundaryDefinition(
                "No trust-blur allowed. Boundary ID required."
            )
        self._boundaries[record.boundary_id] = record

    def get_boundary(self, boundary_id: str) -> Optional[TrustBoundaryRecord]:
        return self._boundaries.get(boundary_id)

    def list_boundaries(self) -> List[TrustBoundaryRecord]:
        return list(self._boundaries.values())
