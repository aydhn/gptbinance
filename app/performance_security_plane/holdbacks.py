from app.performance_security_plane.models import HoldbackRecord

class HoldbackManager:
    def create_holdback(self, holdback_id: str, security_id: str, holdback_type: str) -> HoldbackRecord:
        return HoldbackRecord(
            holdback_id=holdback_id,
            security_id=security_id,
            type=holdback_type,
            lineage_refs=[f"holdback_{holdback_id}"]
        )
