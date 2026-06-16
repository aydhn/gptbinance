from app.waterfall_plane.models import ClawbackTriggerRecord

def register_clawback_trigger(trigger_id: str, condition: str) -> ClawbackTriggerRecord:
    return ClawbackTriggerRecord(trigger_id=trigger_id, condition=condition)
