from app.performance_security_plane.models import FundingStatusRecord
from app.performance_security_plane.enums import FundingClass

class FundingManager:
    def create_funding_status(self, security_id: str, status: FundingClass) -> FundingStatusRecord:
        return FundingStatusRecord(
            security_id=security_id,
            status=status,
            lineage_refs=[f"funding_{security_id}"]
        )
