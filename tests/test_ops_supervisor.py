import pytest
from app.ops.supervisor import SessionSupervisor
from app.ops.models import OpsConfig, OpsRun, SupervisorStatus
from app.ops.enums import OpsMode
from app.ops.startup import SessionStarter
from app.ops.shutdown import SessionShutdown
from app.ops.repository import OpsRepository
from app.ops.storage import OpsStorage
from app.ops.readiness import ReadinessChecker
from app.ops.maintenance import MaintenanceScheduler
from app.ops.incidents import IncidentHandler
from app.ops.recovery import RecoveryCoordinator
from app.ops.reconcile_on_start import StartupReconciler


@pytest.fixture
def repo(tmp_path):
    return OpsRepository(OpsStorage(str(tmp_path)))


def test_supervisor_lifecycle(repo):
    maint = MaintenanceScheduler(repo)
    incidents = IncidentHandler(repo)
    config = OpsConfig(run_id="test-run", mode=OpsMode.PAPER)
    readiness = ReadinessChecker(config, maint, incidents)
    reconciler = StartupReconciler()
    recovery = RecoveryCoordinator(repo, reconciler)
    starter = SessionStarter(repo, readiness, recovery)
    shutdown = SessionShutdown(repo)

    supervisor = SessionSupervisor(repo, starter, shutdown)

    run = OpsRun(run_id="test-run", config=config)
    supervisor.initialize_run(run)

    supervisor.start("test-run")
    db_run = repo.get_run("test-run")
    assert db_run.status == SupervisorStatus.RUNNING

    supervisor.pause("test-run", "testing")
    assert repo.get_run("test-run").status == SupervisorStatus.PAUSED

    supervisor.resume("test-run", "MANUAL_OVERRIDE_CONFIRM")
    assert repo.get_run("test-run").status == SupervisorStatus.RUNNING

    supervisor.drain("test-run")
    assert repo.get_run("test-run").status == SupervisorStatus.DRAINING

    supervisor.stop("test-run")
    assert repo.get_run("test-run").status == SupervisorStatus.STOPPED
