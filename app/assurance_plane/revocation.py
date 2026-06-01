from app.assurance_plane.models import RevocationTriggerRecord
from app.assurance_plane.enums import RevocationClass

def create_revocation_trigger(trigger_id: str, assurance_id: str, rev_class: RevocationClass, conditions: str) -> RevocationTriggerRecord:
    return RevocationTriggerRecord(
        trigger_id=trigger_id,
        assurance_id=assurance_id,
        revocation_class=rev_class,
        conditions=conditions
    )
