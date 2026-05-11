from app.migration_plane.models import MigrationDivergenceReport

class DivergenceManager:
    def generate_report(self, migration_id: str, severity: str, details: dict) -> MigrationDivergenceReport:
         # Implementation for divergence
        return MigrationDivergenceReport(
            migration_id=migration_id,
            severity=severity,
            details=details
        )
