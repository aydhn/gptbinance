from app.performance_security_plane.models import ReserveRecord

class ReserveManager:
    def create_reserve(self, reserve_id: str, security_id: str, reserve_type: str) -> ReserveRecord:
        return ReserveRecord(
            reserve_id=reserve_id,
            security_id=security_id,
            type=reserve_type,
            lineage_refs=[f"reserve_{reserve_id}"]
        )
