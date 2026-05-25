from app.performance_security_plane.models import PriorityRecord
from app.performance_security_plane.enums import PriorityClass

class PriorityManager:
    def create_priority(self, security_id: str, beneficiary_id: str, priority_type: PriorityClass) -> PriorityRecord:
        return PriorityRecord(
            security_id=security_id,
            beneficiary_id=beneficiary_id,
            type=priority_type,
            lineage_refs=[f"priority_{security_id}_{beneficiary_id}"]
        )
