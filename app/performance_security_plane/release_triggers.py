from app.performance_security_plane.models import ReleaseTriggerRecord

class ReleaseTriggerManager:
    def create_release_trigger(self, trigger_id: str, security_id: str, trigger_type: str) -> ReleaseTriggerRecord:
        return ReleaseTriggerRecord(
            trigger_id=trigger_id,
            security_id=security_id,
            type=trigger_type,
            lineage_refs=[f"release_trigger_{trigger_id}"]
        )
