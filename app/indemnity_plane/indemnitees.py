from app.indemnity_plane.models import IndemniteeRecord
def record_indemnitee(indemnity_id: str, identity: str, is_beneficiary: bool) -> IndemniteeRecord:
    return IndemniteeRecord(indemnity_id=indemnity_id, identity=identity, is_beneficiary=is_beneficiary)
