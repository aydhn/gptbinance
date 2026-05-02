import sqlite3
from typing import List, Optional
from app.automation.models import JobDefinition, JobRun, WorkflowDefinition, WorkflowRun


class AutomationStorage:
    def __init__(self, db_path: str = "automation.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS jobs (
                    id TEXT PRIMARY KEY,
                    data TEXT NOT NULL
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS workflows (
                    id TEXT PRIMARY KEY,
                    data TEXT NOT NULL
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS job_runs (
                    id TEXT PRIMARY KEY,
                    job_id TEXT NOT NULL,
                    run_key TEXT,
                    status TEXT NOT NULL,
                    started_at TEXT,
                    data TEXT NOT NULL
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS workflow_runs (
                    id TEXT PRIMARY KEY,
                    workflow_id TEXT NOT NULL,
                    status TEXT NOT NULL,
                    started_at TEXT,
                    data TEXT NOT NULL
                )
            """)

    def save_job(self, job: JobDefinition):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO jobs (id, data) VALUES (?, ?)",
                (job.id, job.model_dump_json()),
            )

    def get_job(self, job_id: str) -> Optional[JobDefinition]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT data FROM jobs WHERE id = ?", (job_id,))
            row = cursor.fetchone()
            if row:
                return JobDefinition.model_validate_json(row[0])
        return None

    def list_jobs(self) -> List[JobDefinition]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT data FROM jobs")
            return [
                JobDefinition.model_validate_json(row[0]) for row in cursor.fetchall()
            ]

    def save_workflow(self, workflow: WorkflowDefinition):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO workflows (id, data) VALUES (?, ?)",
                (workflow.id, workflow.model_dump_json()),
            )

    def get_workflow(self, workflow_id: str) -> Optional[WorkflowDefinition]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT data FROM workflows WHERE id = ?", (workflow_id,)
            )
            row = cursor.fetchone()
            if row:
                return WorkflowDefinition.model_validate_json(row[0])
        return None

    def list_workflows(self) -> List[WorkflowDefinition]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT data FROM workflows")
            return [
                WorkflowDefinition.model_validate_json(row[0])
                for row in cursor.fetchall()
            ]

    def save_job_run(self, run: JobRun):
        started_at_str = run.started_at.isoformat() if run.started_at else None
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO job_runs (id, job_id, run_key, status, started_at, data) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    run.id,
                    run.job_id,
                    run.context.run_key,
                    run.status.value,
                    started_at_str,
                    run.model_dump_json(),
                ),
            )

    def get_job_run(self, run_id: str) -> Optional[JobRun]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT data FROM job_runs WHERE id = ?", (run_id,))
            row = cursor.fetchone()
            if row:
                return JobRun.model_validate_json(row[0])
        return None

    def get_job_run_by_key(self, run_key: str) -> Optional[JobRun]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT data FROM job_runs WHERE run_key = ? ORDER BY started_at DESC LIMIT 1",
                (run_key,),
            )
            row = cursor.fetchone()
            if row:
                return JobRun.model_validate_json(row[0])
        return None

    def get_runs_for_job(self, job_id: str, limit: int = 100) -> List[JobRun]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT data FROM job_runs WHERE job_id = ? ORDER BY started_at DESC LIMIT ?",
                (job_id, limit),
            )
            return [JobRun.model_validate_json(row[0]) for row in cursor.fetchall()]

    def get_all_job_runs(self, limit: int = 1000) -> List[JobRun]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT data FROM job_runs ORDER BY started_at DESC LIMIT ?", (limit,)
            )
            return [JobRun.model_validate_json(row[0]) for row in cursor.fetchall()]

    def save_workflow_run(self, run: WorkflowRun):
        started_at_str = run.started_at.isoformat() if run.started_at else None
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO workflow_runs (id, workflow_id, status, started_at, data) VALUES (?, ?, ?, ?, ?)",
                (
                    run.id,
                    run.workflow_id,
                    run.status.value,
                    started_at_str,
                    run.model_dump_json(),
                ),
            )

    def get_workflow_run(self, run_id: str) -> Optional[WorkflowRun]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT data FROM workflow_runs WHERE id = ?", (run_id,)
            )
            row = cursor.fetchone()
            if row:
                return WorkflowRun.model_validate_json(row[0])
        return None
