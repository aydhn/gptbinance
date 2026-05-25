from app.performance_security_plane.models import SegregationRecord

class SegregationManager:
    def create_segregation(self, security_id: str, status: str) -> SegregationRecord:
        return SegregationRecord(
            security_id=security_id,
            status=status,
            lineage_refs=[f"segregation_{security_id}"]
        )
