import pytest
from app.ops.readiness import ReadinessChecker
from app.ops.models import OpsConfig
from app.ops.enums import OpsMode, ReadinessVerdict
from app.ops.maintenance import MaintenanceScheduler
from app.ops.incidents import IncidentHandler
from app.ops.repository import OpsRepository
from app.ops.storage import OpsStorage
from datetime import datetime, timedelta


@pytest.fixture
def repo(tmp_path):
    storage = OpsStorage(str(tmp_path))
    return OpsRepository(storage)


def test_readiness_passes_when_clean(repo):
    maint = MaintenanceScheduler(repo)
    incidents = IncidentHandler(repo)
    config = OpsConfig(run_id="run-1", mode=OpsMode.PAPER)
    checker = ReadinessChecker(config, maint, incidents)

    report = checker.check_all("run-1")
    assert report.overall_verdict == ReadinessVerdict.PASS


def test_readiness_fails_with_maintenance(repo):
    maint = MaintenanceScheduler(repo)
    incidents = IncidentHandler(repo)
    config = OpsConfig(run_id="run-2", mode=OpsMode.PAPER)

    # Schedule active maintenance
    now = datetime.utcnow()
    maint.schedule_window(
        now - timedelta(minutes=10), now + timedelta(minutes=10), "Test Window"
    )

    checker = ReadinessChecker(config, maint, incidents)
    report = checker.check_all("run-2")

    assert report.overall_verdict == ReadinessVerdict.FAIL
