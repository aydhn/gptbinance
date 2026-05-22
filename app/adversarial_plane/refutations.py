from typing import List, Optional
from app.adversarial_plane.models import RefutationRecord

def create_refutation(refutation_id: str, refutation_type: str, unresolved_suspicion_caveats: Optional[str] = None, lineage_refs: Optional[List[str]] = None) -> RefutationRecord:
    valid_types = {"partial", "full", "scope_bounded"}
    if refutation_type not in valid_types:
        raise ValueError(f"Invalid refutation type. Must be one of {valid_types}")
    return RefutationRecord(
        refutation_id=refutation_id,
        refutation_type=refutation_type,
        unresolved_suspicion_caveats=unresolved_suspicion_caveats,
        lineage_refs=lineage_refs or []
    )

class RefutationManager:
    def __init__(self):
        self._refutations = {}

    def add_refutation(self, ref: RefutationRecord):
        self._refutations[ref.refutation_id] = ref

    def get_refutation(self, refutation_id: str) -> Optional[RefutationRecord]:
        return self._refutations.get(refutation_id)

    def list_refutations(self) -> List[RefutationRecord]:
        return list(self._refutations.values())
