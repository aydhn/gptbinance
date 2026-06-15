from app.indemnity_plane.models import IndemnityDebtRecord
def record_debt(indemnity_id: str, debt_class: str, severity: str) -> IndemnityDebtRecord:
    return IndemnityDebtRecord(indemnity_id=indemnity_id, debt_class=debt_class, severity=severity)
