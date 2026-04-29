from app.ops.models import RecoveryResult
from app.ops.base import RecoveryCoordinatorBase
from app.ops.reconcile_on_start import StartupReconciler
from app.ops.repository import OpsRepository


class RecoveryCoordinator(RecoveryCoordinatorBase):
    def __init__(self, repository: OpsRepository, reconciler: StartupReconciler):
        self.repository = repository
        self.reconciler = reconciler

    def coordinate_recovery(self, run_id: str) -> RecoveryResult:
        verdict = self.reconciler.reconcile(run_id)
        result = RecoveryResult(
            run_id=run_id,
            verdict=verdict,
            details="Recovery and reconciliation complete.",
        )
        self.repository.save_recovery_result(result)
        return result
