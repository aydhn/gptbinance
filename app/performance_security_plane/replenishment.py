from app.performance_security_plane.models import ReplenishmentDutyRecord

class ReplenishmentManager:
    def create_replenishment_duty(self, duty_id: str, security_id: str, duty_type: str) -> ReplenishmentDutyRecord:
        return ReplenishmentDutyRecord(
            duty_id=duty_id,
            security_id=security_id,
            type=duty_type,
            lineage_refs=[f"replenishment_{duty_id}"]
        )
