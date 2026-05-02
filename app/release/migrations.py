from typing import List
from app.release.models import MigrationPlan, MigrationRecord
from app.release.migration_registry import MigrationRegistry
from app.release.enums import MigrationDirection, MigrationSeverity
from datetime import datetime, timezone
import logging

logger = logging.getLogger(__name__)


class MigrationExecutor:
    def __init__(self):
        self.registry = MigrationRegistry()

    def create_plan(
        self, source: str, target: str, direction: MigrationDirection
    ) -> MigrationPlan:
        path = self.registry.get_path(source, target)
        mig_ids = [m.id for m in path]
        sev = MigrationSeverity.LOW
        for m in path:
            if (
                m.severity == MigrationSeverity.HIGH
                or m.severity == MigrationSeverity.DESTRUCTIVE
            ):
                sev = m.severity
        return MigrationPlan(
            source_version=source,
            target_version=target,
            migrations_to_apply=mig_ids,
            estimated_severity=sev,
            dry_run=True,
        )

    def execute(self, plan: MigrationPlan) -> List[MigrationRecord]:
        records = []
        for mid in plan.migrations_to_apply:
            logger.info(f"Executing migration {mid} (dry_run={plan.dry_run})")
            records.append(
                MigrationRecord(
                    migration_id=mid,
                    direction=MigrationDirection.UPGRADE,
                    severity=plan.estimated_severity,
                    applied_at=datetime.now(timezone.utc),
                    success=True,
                )
            )
        return records
