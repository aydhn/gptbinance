from typing import List
from datetime import datetime
from app.migrations.models import MigrationDebtRecord, MigrationDefinition
from app.migrations.enums import MigrationDomain, MigrationStatus, MigrationSeverity


class MigrationDebtGovernance:
    def __init__(self):
        self._debt_records: List[MigrationDebtRecord] = []

    def record_debt(
        self, migration: MigrationDefinition, status: MigrationStatus, impact: str
    ) -> None:
        record = MigrationDebtRecord(
            migration_id=migration.id,
            domain=migration.domain,
            severity=migration.severity,
            status=status,
            recorded_at=datetime.now(),
            impact_summary=impact,
        )
        self._debt_records.append(record)

    def get_all_debt(self) -> List[MigrationDebtRecord]:
        return self._debt_records

    def get_debt_by_domain(self, domain: MigrationDomain) -> List[MigrationDebtRecord]:
        return [r for r in self._debt_records if r.domain == domain]

    def is_debt_critical(self) -> bool:
        return any(r.severity == MigrationSeverity.CRITICAL for r in self._debt_records)
