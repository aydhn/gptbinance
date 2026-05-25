from app.performance_security_plane.models import EscrowRecord

class EscrowManager:
    def create_escrow(self, escrow_id: str, security_id: str, escrow_type: str) -> EscrowRecord:
        return EscrowRecord(
            escrow_id=escrow_id,
            security_id=security_id,
            type=escrow_type,
            lineage_refs=[f"escrow_{escrow_id}"]
        )
