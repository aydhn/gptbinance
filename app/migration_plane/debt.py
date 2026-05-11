from app.migration_plane.models import MigrationDebtRecord
from app.migration_plane.enums import DebtClass

class DebtManager:
    def record_debt(self, migration_id: str, debt_class: DebtClass, severity: str, details: dict) -> MigrationDebtRecord:
         # Implementation for debt tracking
        return MigrationDebtRecord(
            migration_id=migration_id,
            debt_class=debt_class,
            severity=severity,
            details=details
        )
