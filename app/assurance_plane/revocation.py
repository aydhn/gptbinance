from app.assurance_plane.models import RevocationTriggerRecord
from app.assurance_plane.enums import RevocationClass

def create_revocation_trigger(trigger_id: str, assurance_id: str, rev_class: RevocationClass, conditions: str) -> RevocationTriggerRecord:
    return RevocationTriggerRecord(
        trigger_id=trigger_id,
        assurance_id=assurance_id,
        revocation_class=rev_class,
        conditions=conditions
    )

def revoke_assurance_with_accountability(assurance_id: str, accountability_id: str = None):
    """
    Revokes an assurance.
    If accountability_id is missing, explicit caution is generated (Phase 135).
    """
    if not accountability_id:
        return {"status": "caution", "message": "Assurance revoked without accountable subject mapping."}
    return {"status": "success", "revoked": assurance_id, "accountability": accountability_id}
