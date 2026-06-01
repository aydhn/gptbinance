from app.assurance_plane.models import SufficiencyRecord
from app.assurance_plane.enums import SufficiencyClass

def create_sufficiency(sufficiency_id: str, claim_id: str, pack_id: str, sufficiency_class: SufficiencyClass, notes: str) -> SufficiencyRecord:
    return SufficiencyRecord(
        sufficiency_id=sufficiency_id,
        claim_id=claim_id,
        pack_id=pack_id,
        sufficiency_class=sufficiency_class,
        evaluation_notes=notes
    )
