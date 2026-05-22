from app.commitment_plane.models import CommitmentDebtRecord

class DebtManager:
    @staticmethod
    def create_debt_record(debt_type: str, severity: str, interest: str) -> CommitmentDebtRecord:
        valid_types = ['ownerless', 'silent_extension', 'weak_backing', 'relief_abuse', 'breached_undischarged']
        if debt_type not in valid_types:
            raise ValueError(f"Invalid debt type. Must be one of {valid_types}")

        return CommitmentDebtRecord(
            debt_type=debt_type,
            severity=severity,
            interest=interest
        )
