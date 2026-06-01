from app.assurance_plane.models import AssuranceDebtRecord

def create_debt(debt_id: str, assurance_id: str, debt_type: str, severity: str) -> AssuranceDebtRecord:
    return AssuranceDebtRecord(
        debt_id=debt_id,
        assurance_id=assurance_id,
        debt_type=debt_type,
        severity=severity
    )
