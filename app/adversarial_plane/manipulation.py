from typing import List, Optional
from app.adversarial_plane.models import ManipulationRecord

def create_manipulation(manipulation_id: str, manipulation_type: str, caveats: str, lineage_refs: Optional[List[str]] = None) -> ManipulationRecord:
    valid_types = {"metric", "workflow", "evidence_ordering", "rollout_narrative"}
    if manipulation_type not in valid_types:
        raise ValueError(f"Invalid manipulation type. Must be one of {valid_types}")
    return ManipulationRecord(
        manipulation_id=manipulation_id,
        manipulation_type=manipulation_type,
        caveats=caveats,
        lineage_refs=lineage_refs or []
    )

class ManipulationManager:
    def __init__(self):
        self._manipulations = {}

    def add_manipulation(self, man: ManipulationRecord):
        self._manipulations[man.manipulation_id] = man

    def get_manipulation(self, manipulation_id: str) -> Optional[ManipulationRecord]:
        return self._manipulations.get(manipulation_id)

    def list_manipulations(self) -> List[ManipulationRecord]:
        return list(self._manipulations.values())
