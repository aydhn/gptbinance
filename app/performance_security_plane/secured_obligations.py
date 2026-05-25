from app.performance_security_plane.models import SecuredObligationRecord
from app.performance_security_plane.enums import SecuredObligationClass

class SecuredObligationManager:
    def create_secured_obligation(self, obligation_id: str, security_refs: list[str], posture: SecuredObligationClass) -> SecuredObligationRecord:
        return SecuredObligationRecord(
            obligation_id=obligation_id,
            security_refs=security_refs,
            posture=posture,
            lineage_refs=[f"obligation_{obligation_id}"]
        )
