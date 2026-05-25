from app.performance_security_plane.models import SupportUndertakingRecord

class SupportUndertakingManager:
    def create_support_undertaking(self, undertaking_id: str, security_id: str, undertaking_type: str) -> SupportUndertakingRecord:
        return SupportUndertakingRecord(
            undertaking_id=undertaking_id,
            security_id=security_id,
            type=undertaking_type,
            lineage_refs=[f"undertaking_{undertaking_id}"]
        )
