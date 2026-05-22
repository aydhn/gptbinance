from typing import List, Optional
from app.adversarial_plane.models import CollusionRecord

def create_collusion(collusion_id: str, collusion_type: str, caveats: str, lineage_refs: Optional[List[str]] = None) -> CollusionRecord:
    valid_types = {"human_human", "human_agent", "partner_local", "tacit"}
    if collusion_type not in valid_types:
        raise ValueError(f"Invalid collusion type. Must be one of {valid_types}")
    return CollusionRecord(
        collusion_id=collusion_id,
        collusion_type=collusion_type,
        caveats=caveats,
        lineage_refs=lineage_refs or []
    )

class CollusionManager:
    def __init__(self):
        self._collusions = {}

    def add_collusion(self, coll: CollusionRecord):
        self._collusions[coll.collusion_id] = coll

    def get_collusion(self, collusion_id: str) -> Optional[CollusionRecord]:
        return self._collusions.get(collusion_id)

    def list_collusions(self) -> List[CollusionRecord]:
        return list(self._collusions.values())
