import logging
from app.ops.base import SupervisorBase
from app.ops.models import OpsRun, SupervisorStatus, OpsAuditRecord
from app.ops.startup import SessionStarter
from app.ops.shutdown import SessionShutdown
from app.ops.repository import OpsRepository
from app.observability.telemetry import ingester
from app.observability.enums import ComponentType, AlertSeverity


class SessionSupervisor(SupervisorBase):
    def __init__(
        self,
        repository: OpsRepository,
        starter: SessionStarter,
        shutdown: SessionShutdown,
    ):
        self.repository = repository
        self.starter = starter
        self.shutdown = shutdown
        self._current_run: OpsRun | None = None

    def initialize_run(self, run: OpsRun) -> None:
        self._current_run = run
        self.repository.save_run(run)

    def start(self, run_id: str) -> None:
        if not self._current_run or self._current_run.run_id != run_id:
            raise ValueError("Run not initialized.")

        self._current_run.status = SupervisorStatus.STARTING
        self._audit(run_id, "start_initiated")

        if self.starter.perform_startup(self._current_run):
            self._current_run.status = SupervisorStatus.RUNNING
            self._audit(run_id, "start_success")
        else:
            self._current_run.status = SupervisorStatus.HALTED_ON_ERROR
            self._audit(run_id, "start_failed")
        self.repository.save_run(self._current_run)

    def pause(self, run_id: str, reason: str) -> None:
        if self._current_run and self._current_run.run_id == run_id:
            self._current_run.status = SupervisorStatus.PAUSED
            self._audit(run_id, f"paused: {reason}")
            self.repository.save_run(self._current_run)

    def resume(self, run_id: str, clearance_code: str) -> None:
        if self._current_run and self._current_run.run_id == run_id:
            if self._current_run.status == SupervisorStatus.PAUSED:
                self._current_run.status = SupervisorStatus.RUNNING
                self._audit(run_id, f"resumed with code: {clearance_code}")
                self.repository.save_run(self._current_run)

    def drain(self, run_id: str) -> None:
        if self._current_run and self._current_run.run_id == run_id:
            self._current_run.status = SupervisorStatus.DRAINING
            self._audit(run_id, "drain_initiated")
            self.shutdown.perform_drain(run_id)
            self.repository.save_run(self._current_run)

    def stop(self, run_id: str) -> None:
        if self._current_run and self._current_run.run_id == run_id:
            self._current_run.status = SupervisorStatus.STOPPING
            self._audit(run_id, "stop_initiated")
            self.shutdown.perform_shutdown(run_id)
            self._current_run.status = SupervisorStatus.STOPPED
            self.repository.save_run(self._current_run)

    def _audit(self, run_id: str, action: str) -> None:
        record = OpsAuditRecord(run_id=run_id, action=action, details="")
        self.repository.append_audit_record(record)
        ingester.capture_event(
            event_type=f"supervisor_{action}",
            component=ComponentType.SUPERVISOR,
            details={"run_id": run_id, "action": action},
            severity=AlertSeverity.INFO,
            run_id=run_id,
        )

    def flatten_live(self, run_id: str, reason: str) -> None:
        if self._current_run and self._current_run.run_id == run_id:
            self._audit(run_id, f"flatten_live_initiated: {reason}")
            # Placeholder for actual LiveRuntime flatten invocation
            pass

    def rollback_live(self, run_id: str, reason: str) -> None:
        if self._current_run and self._current_run.run_id == run_id:
            self._audit(run_id, f"rollback_live_initiated: {reason}")
            # Placeholder for actual LiveRuntime rollback invocation
            pass


class Supervisor:
    def halt(self, reason: str):
        logging.getLogger(__name__).error(f"SUPERVISOR HALTED SYSTEM: {reason}")

    def pause(self, reason: str):
        logging.getLogger(__name__).warning(f"SUPERVISOR PAUSED SYSTEM: {reason}")

    def drain(self, reason: str):
        logging.getLogger(__name__).info(f"SUPERVISOR DRAINING: {reason}")
