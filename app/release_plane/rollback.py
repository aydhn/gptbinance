from datetime import timezone
from app.release_plane.models import RollbackPackage, ReleaseRef, RollbackExecutionRecord
from app.release_plane.exceptions import RollbackViolation
from typing import List
from datetime import datetime
import uuid

class RollbackManager:
    def __init__(self):
        self._packages = {}
        self._executions = []

    def create_package(self, target_release_id: str, reversible_entries: List[str], prerequisites: List[str]) -> RollbackPackage:
        if not reversible_entries:
             raise RollbackViolation("Rollback package must specify reversible entries. No fake rollback promises.")

        pkg = RollbackPackage(
            package_id=f"rbk-{uuid.uuid4().hex[:8]}",
            target_release_ref=ReleaseRef(release_id=target_release_id),
            reversible_entries=reversible_entries,
            prerequisites=prerequisites,
            lineage_refs=[]
        )
        self._packages[pkg.package_id] = pkg
        return pkg

    def execute_rollback(self, package_id: str) -> RollbackExecutionRecord:
        if package_id not in self._packages:
             raise RollbackViolation("Invalid rollback package ID.")

        # Check prerequisites in real implementation

        record = RollbackExecutionRecord(
            execution_id=f"rbk-exec-{uuid.uuid4().hex[:8]}",
            package_id=package_id,
            executed_at=datetime.now(timezone.utc)
        )
        self._executions.append(record)
        return record
