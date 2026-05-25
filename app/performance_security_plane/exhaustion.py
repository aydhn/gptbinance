from app.performance_security_plane.models import ExhaustionRecord
from app.performance_security_plane.enums import ExhaustionClass

class ExhaustionManager:
    def create_exhaustion(self, security_id: str, exhaustion_type: ExhaustionClass) -> ExhaustionRecord:
        return ExhaustionRecord(
            security_id=security_id,
            type=exhaustion_type,
            lineage_refs=[f"exhaustion_{security_id}"]
        )
