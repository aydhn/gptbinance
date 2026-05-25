from app.settlement_plane.models import AuthorityToSettleRecord

def evaluate_authority(authority: AuthorityToSettleRecord):
    if authority.defects:
        return {"status": "defective", "authority_id": authority.id, "defects": authority.defects}
    return {"status": "valid", "authority_id": authority.id}
