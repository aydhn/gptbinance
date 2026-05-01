from enum import Enum


class JobType(str, Enum):
    DATA_REFRESH = "data_refresh"
    FEATURE_REFRESH = "feature_refresh"
    GOVERNANCE_REFRESH = "governance_refresh"
    ANALYTICS_SUMMARY = "analytics_summary"
    HEALTH_CHECK = "health_check"
    RECONCILIATION = "reconciliation"
    BACKUP = "backup"
    READINESS_CHECK = "readiness_check"
    DRIFT_CHECK = "drift_check"
    PAPER_SMOKE = "paper_smoke"


class WorkflowType(str, Enum):
    NIGHTLY_RESEARCH_REFRESH = "nightly_research_refresh"
    MORNING_READINESS = "morning_readiness"
    WEEKLY_ANALYTICS = "weekly_analytics"
    POST_INCIDENT_DIAGNOSTICS = "post_incident_diagnostics"
    PRE_ROLLOUT_VALIDATION = "pre_rollout_validation"


class ScheduleType(str, Enum):
    INTERVAL = "interval"
    FIXED_TIME = "fixed_time"
    CRON = "cron"
    MANUAL = "manual"


class RunStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"
    DEFERRED = "deferred"
    BLOCKED = "blocked"
    CANCELED = "canceled"


class RetryVerdict(str, Enum):
    RETRY = "retry"
    EXHAUSTED = "exhausted"
    NON_RETRYABLE = "non_retryable"


class GateVerdict(str, Enum):
    PASS = "pass"
    CAUTION = "caution"
    FAIL = "fail"


class PreconditionAction(str, Enum):
    ALLOW = "allow"
    DEFER = "defer"
    SKIP = "skip"
    BLOCK = "block"
    ESCALATE = "escalate"


class TriggerType(str, Enum):
    TIME = "time"
    MANUAL = "manual"
    EVENT = "event"


class QuietHoursVerdict(str, Enum):
    ALLOW = "allow"
    DEFER = "defer"


class MaintenanceAction(str, Enum):
    ALLOW = "allow"
    DEFER = "defer"
    BLOCK = "block"


class AutomationSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"
