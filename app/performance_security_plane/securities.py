from app.performance_security_plane.models import PerformanceSecurityRecord

class SecurityManager:
    def create_security_record(self, security_id: str, state: str, proof_notes: str) -> PerformanceSecurityRecord:
        return PerformanceSecurityRecord(
            security_id=security_id,
            state=state,
            proof_notes=proof_notes,
            lineage_refs=[f"created_for_{security_id}"]
        )
