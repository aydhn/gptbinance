from app.migration_plane.models import BackfillExecutionRecord

class BackfillManager:
    def execute_backfill(self, migration_id: str, is_required: bool) -> BackfillExecutionRecord:
        # Implementation for executing backfill
        return BackfillExecutionRecord(
            migration_id=migration_id,
            is_required=is_required,
            is_successful=True,
            details={"status": "completed"}
        )
