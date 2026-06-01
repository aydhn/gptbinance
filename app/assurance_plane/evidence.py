from app.assurance_plane.models import EvidencePackRecord, EvidenceItemRecord
from app.assurance_plane.enums import EvidenceClass

def create_evidence_item(item_id: str, evidence_class: EvidenceClass, source: str) -> EvidenceItemRecord:
    return EvidenceItemRecord(
        item_id=item_id,
        evidence_class=evidence_class,
        source=source
    )

def create_evidence_pack(pack_id: str, items: list[EvidenceItemRecord]) -> EvidencePackRecord:
    return EvidencePackRecord(
        pack_id=pack_id,
        items=items
    )
