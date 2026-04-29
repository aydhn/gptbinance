from app.ops.models import RecoveryVerdict


class StartupReconciler:
    def reconcile(self, run_id: str) -> RecoveryVerdict:
        return RecoveryVerdict.RECOVERABLE
