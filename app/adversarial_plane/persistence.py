from typing import List, Optional
from app.adversarial_plane.models import PersistenceRecord

def create_persistence(persistence_id: str, persistence_level: str, caveats: str, lineage_refs: Optional[List[str]] = None) -> PersistenceRecord:
    valid_levels = {"one_shot", "recurring", "latent", "normalized"}
    if persistence_level not in valid_levels:
        raise ValueError(f"Invalid persistence level. Must be one of {valid_levels}")
    return PersistenceRecord(
        persistence_id=persistence_id,
        persistence_level=persistence_level,
        caveats=caveats,
        lineage_refs=lineage_refs or []
    )

class PersistenceManager:
    def __init__(self):
        self._persistences = {}

    def add_persistence(self, per: PersistenceRecord):
        self._persistences[per.persistence_id] = per

    def get_persistence(self, persistence_id: str) -> Optional[PersistenceRecord]:
        return self._persistences.get(persistence_id)

    def list_persistences(self) -> List[PersistenceRecord]:
        return list(self._persistences.values())
