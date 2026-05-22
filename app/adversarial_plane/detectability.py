from typing import List, Optional
from app.adversarial_plane.models import DetectabilityRecord

def create_detectability(detectability_id: str, detectability_level: str, proof_notes: str, lineage_refs: Optional[List[str]] = None) -> DetectabilityRecord:
    valid_levels = {"easy", "weak", "stealthy", "post_hoc"}
    if detectability_level not in valid_levels:
        raise ValueError(f"Invalid detectability level. Must be one of {valid_levels}")
    return DetectabilityRecord(
        detectability_id=detectability_id,
        detectability_level=detectability_level,
        proof_notes=proof_notes,
        lineage_refs=lineage_refs or []
    )

class DetectabilityManager:
    def __init__(self):
        self._detectabilities = {}

    def add_detectability(self, det: DetectabilityRecord):
        self._detectabilities[det.detectability_id] = det

    def get_detectability(self, detectability_id: str) -> Optional[DetectabilityRecord]:
        return self._detectabilities.get(detectability_id)

    def list_detectabilities(self) -> List[DetectabilityRecord]:
        return list(self._detectabilities.values())
