from datetime import timezone
from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

from app.automation.enums import (
    JobType,
    WorkflowType,
    ScheduleType,
    RunStatus,
    PreconditionAction,
    TriggerType,
)


class RetryPolicy(BaseModel):
    max_attempts: int = 0
    backoff_seconds: int = 60
    exponential: bool = False
    retryable_exceptions: List[str] = Field(default_factory=list)


class QuietHoursPolicy(BaseModel):
    enabled: bool = False
    start_hour: int = 0
    end_hour: int = 0
    defer_until_end: bool = True


class MaintenanceAwarePolicy(BaseModel):
    allow_during_maintenance: bool = False
    defer_during_maintenance: bool = True


class JobSchedule(BaseModel):
    type: ScheduleType
    expression: str  # e.g. "3600" for interval, "daily@02:30", "* * * * *" for cron
    timezone: str = "UTC"


class JobDefinition(BaseModel):
    id: str
    type: JobType
    name: str
    schedule: Optional[JobSchedule] = None
    retry_policy: RetryPolicy = Field(default_factory=RetryPolicy)
    quiet_hours: QuietHoursPolicy = Field(default_factory=QuietHoursPolicy)
    maintenance_policy: MaintenanceAwarePolicy = Field(
        default_factory=MaintenanceAwarePolicy
    )
    inputs: Dict[str, Any] = Field(default_factory=dict)
    live_affecting: bool = False
    paused: bool = False
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )  # Will replace in logic if needed


class JobRunContext(BaseModel):
    trigger_type: TriggerType
    triggered_by: str = "system"
    run_key: str  # For idempotency


class JobRun(BaseModel):
    id: str
    job_id: str
    job_type: JobType
    status: RunStatus = RunStatus.PENDING
    context: JobRunContext
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    duration_seconds: Optional[float] = None
    attempt: int = 1
    error_message: Optional[str] = None
    artifacts: Dict[str, Any] = Field(default_factory=dict)
    rationale: Optional[str] = None


class DependencySpec(BaseModel):
    job_id: str
    require_success: bool = True


class WorkflowStep(BaseModel):
    id: str
    job_id: str
    dependencies: List[str] = Field(default_factory=list)  # List of step ids


class WorkflowDefinition(BaseModel):
    id: str
    type: WorkflowType
    name: str
    schedule: Optional[JobSchedule] = None
    steps: List[WorkflowStep] = Field(default_factory=list)
    paused: bool = False


class WorkflowRun(BaseModel):
    id: str
    workflow_id: str
    status: RunStatus = RunStatus.PENDING
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    step_runs: Dict[str, str] = Field(default_factory=dict)  # step_id -> job_run_id


class RunHistoryEntry(BaseModel):
    run_id: str
    job_id: str
    status: RunStatus
    started_at: datetime
    duration_seconds: Optional[float]
    attempt: int
    error: Optional[str]


class AutomationConfig(BaseModel):
    global_pause: bool = False


class GateCheckResult(BaseModel):
    passed: bool
    rationale: str
    action: PreconditionAction


class PreconditionCheck(BaseModel):
    name: str
    result: GateCheckResult


class AutomationSummary(BaseModel):
    total_jobs: int
    due_jobs: int
    paused_jobs: int
    recent_failures: int
    next_runs: List[Dict[str, Any]]


class AutomationAuditRecord(BaseModel):
    id: str
    timestamp: datetime
    action: str
    details: str
