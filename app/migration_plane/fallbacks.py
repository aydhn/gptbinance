from app.migration_plane.models import FallbackRecord

class FallbackManager:
    def execute_fallback(self, migration_id: str) -> FallbackRecord:
         # Implementation for fallback
        return FallbackRecord(
            migration_id=migration_id,
            is_successful=True,
            details={"status": "completed"}
        )
