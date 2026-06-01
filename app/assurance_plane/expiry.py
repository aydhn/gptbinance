from app.assurance_plane.models import ExpiryRecord

def create_expiry(expiry_id: str, assurance_id: str, is_expired: bool, reason: str) -> ExpiryRecord:
    return ExpiryRecord(
        expiry_id=expiry_id,
        assurance_id=assurance_id,
        is_expired=is_expired,
        reason=reason
    )
