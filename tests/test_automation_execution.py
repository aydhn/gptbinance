from app.automation.enums import JobType, TriggerType, RunStatus
from app.automation.execution import AutomationEngine
from app.automation.models import JobDefinition
from app.automation.storage import AutomationStorage
from app.automation.repository import AutomationRepository
from app.automation.jobs import DataRefreshExecutor
import tempfile
import os


def test_job_execution():
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        db_path = tf.name

    try:
        storage = AutomationStorage(db_path)
        repo = AutomationRepository(storage)
        executors = {JobType.DATA_REFRESH: DataRefreshExecutor()}

        engine = AutomationEngine(repo, executors)

        job = JobDefinition(id="job1", type=JobType.DATA_REFRESH, name="Test Job")
        repo.save_job(job)

        run = engine.run_job(job, trigger=TriggerType.MANUAL)
        assert run.status == RunStatus.SUCCESS
        assert "rows_updated" in run.artifacts
    finally:
        os.remove(db_path)


def test_paused_job_execution():
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        db_path = tf.name

    try:
        storage = AutomationStorage(db_path)
        repo = AutomationRepository(storage)
        executors = {JobType.DATA_REFRESH: DataRefreshExecutor()}

        engine = AutomationEngine(repo, executors)

        job = JobDefinition(
            id="job2", type=JobType.DATA_REFRESH, name="Test Job", paused=True
        )
        repo.save_job(job)

        run = engine.run_job(job, trigger=TriggerType.TIME)
        assert run.status == RunStatus.SKIPPED
    finally:
        os.remove(db_path)
