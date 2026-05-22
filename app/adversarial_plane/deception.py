from typing import List, Optional
from app.adversarial_plane.models import DeceptionRecord

def create_deception(deception_id: str, deception_type: str, proof_notes: str, lineage_refs: Optional[List[str]] = None) -> DeceptionRecord:
    valid_types = {"partial_truth", "semantic", "stale_as_fresh", "proxy_safe"}
    if deception_type not in valid_types:
        raise ValueError(f"Invalid deception type. Must be one of {valid_types}")
    return DeceptionRecord(
        deception_id=deception_id,
        deception_type=deception_type,
        proof_notes=proof_notes,
        lineage_refs=lineage_refs or []
    )

class DeceptionManager:
    def __init__(self):
        self._deceptions = {}

    def add_deception(self, dec: DeceptionRecord):
        self._deceptions[dec.deception_id] = dec

    def get_deception(self, deception_id: str) -> Optional[DeceptionRecord]:
        return self._deceptions.get(deception_id)

    def list_deceptions(self) -> List[DeceptionRecord]:
        return list(self._deceptions.values())
