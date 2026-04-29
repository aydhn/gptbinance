from app.ops.models import OpsRun, ReadinessVerdict, RecoveryVerdict
from app.ops.readiness import ReadinessChecker
from app.ops.recovery import RecoveryCoordinator
from app.ops.repository import OpsRepository


class SessionStarter:
    def __init__(
        self,
        repository: OpsRepository,
        readiness: ReadinessChecker,
        recovery: RecoveryCoordinator,
    ):
        self.repository = repository
        self.readiness = readiness
        self.recovery = recovery

    def perform_startup(self, run: OpsRun) -> bool:
        print(f"[STARTUP] Starting OpsRun: {run.run_id}")
        report = self.readiness.check_all(run.run_id)
        self.repository.save_readiness_report(report)
        if report.overall_verdict == ReadinessVerdict.FAIL:
            print("[STARTUP] Readiness failed. Halting startup.")
            return False

        rec_res = self.recovery.coordinate_recovery(run.run_id)
        if rec_res.verdict == RecoveryVerdict.HALT:
            print("[STARTUP] Recovery failed with HALT. Cannot start safely.")
            return False

        print("[STARTUP] Startup sequence complete. Ready to run.")
        return True
