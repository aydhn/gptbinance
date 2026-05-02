from app.release.models import DependencyLockSummary
from app.release.enums import DependencyStatus


class DependencyManager:
    def get_lock_summary(self) -> DependencyLockSummary:
        return DependencyLockSummary(
            fingerprint="test_fingerprint",
            status=DependencyStatus.SYNCED,
            drift_details=[],
        )
