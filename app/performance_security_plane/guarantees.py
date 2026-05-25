from app.performance_security_plane.models import GuaranteeRecord
from app.performance_security_plane.enums import GuaranteeClass

class GuaranteeManager:
    def create_guarantee(self, guarantee_id: str, security_id: str, guarantee_type: GuaranteeClass) -> GuaranteeRecord:
        return GuaranteeRecord(
            guarantee_id=guarantee_id,
            security_id=security_id,
            type=guarantee_type,
            lineage_refs=[f"guarantee_{guarantee_id}"]
        )
