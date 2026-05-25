from app.performance_security_plane.models import SecurityDebtRecord

class DebtManager:
    def create_debt_record(self, debt_id: str, security_id: str, debt_type: str, severity: str) -> SecurityDebtRecord:
        return SecurityDebtRecord(
            debt_id=debt_id,
            security_id=security_id,
            type=debt_type,
            severity=severity
        )
