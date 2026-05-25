from app.performance_security_plane.models import BeneficiaryRecord

class BeneficiaryManager:
    def create_beneficiary(self, beneficiary_id: str, security_id: str, beneficiary_type: str) -> BeneficiaryRecord:
        return BeneficiaryRecord(
            beneficiary_id=beneficiary_id,
            security_id=security_id,
            type=beneficiary_type,
            lineage_refs=[f"beneficiary_{beneficiary_id}"]
        )
