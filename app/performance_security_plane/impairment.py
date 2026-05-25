from app.performance_security_plane.models import ImpairmentRecord
from app.performance_security_plane.enums import ImpairmentClass

class ImpairmentManager:
    def create_impairment(self, security_id: str, impairment_type: ImpairmentClass) -> ImpairmentRecord:
        return ImpairmentRecord(
            security_id=security_id,
            type=impairment_type,
            lineage_refs=[f"impairment_{security_id}"]
        )
