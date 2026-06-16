from app.waterfall_plane.models import AntiDuplicationRecord

def register_anti_duplication(record_id: str, claim_id: str, description: str) -> AntiDuplicationRecord:
    return AntiDuplicationRecord(record_id=record_id, claim_id=claim_id, description=description)
