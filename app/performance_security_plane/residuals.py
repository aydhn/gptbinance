from app.performance_security_plane.models import ResidualUndersecurityRecord

class ResidualsManager:
    def create_residual_undersecurity(self, security_id: str, residual_type: str, gap_amount: float) -> ResidualUndersecurityRecord:
        return ResidualUndersecurityRecord(
            security_id=security_id,
            type=residual_type,
            gap_amount=gap_amount,
            lineage_refs=[f"residual_{security_id}"]
        )
