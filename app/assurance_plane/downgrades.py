from app.assurance_plane.models import DowngradeRecord

def create_downgrade(downgrade_id: str, assurance_id: str, reason: str) -> DowngradeRecord:
    return DowngradeRecord(
        downgrade_id=downgrade_id,
        assurance_id=assurance_id,
        reason=reason
    )
