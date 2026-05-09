from enum import Enum

class WorkflowClass(str, Enum):
    PRODUCTION = "production"
    EXPLORATORY = "exploratory"
    BACKFILL = "backfill"
    RECOVERY = "recovery"

class JobClass(str, Enum):
    DATA_REFRESH = "data_refresh"
    FEATURE_BUILD = "feature_build"
    MODEL_INFERENCE = "model_inference"
    ALLOCATION = "allocation"
    EXECUTION = "execution"
    RECONCILIATION = "reconciliation"
    RISK_REFRESH = "risk_refresh"
    PERFORMANCE_ROLLUP = "performance_rollup"

class RunState(str, Enum):
    QUEUED = "queued"
    GATED_WAIT = "gated_wait"
    READY = "ready"
    RUNNING = "running"
    PARTIALLY_COMPLETED = "partially_completed"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    BLOCKED = "blocked"
    RESUMED = "resumed"
    RERUN_SUPERSEDED = "rerun_superseded"

class TriggerClass(str, Enum):
    MANUAL = "manual"
    SCHEDULE = "schedule"
    DATA_ARRIVAL = "data_arrival"
    INCIDENT = "incident"
    ACTIVATION = "activation"
    REPLAY = "replay"

class ScheduleClass(str, Enum):
    SESSION_OPEN = "session_open"
    SESSION_CLOSE = "session_close"
    ROLLING = "rolling"
    EVENT_COUPLED = "event_coupled"
    MANUAL_ONLY = "manual_only"
    INCIDENT_DRIVEN = "incident_driven"

class WindowClass(str, Enum):
    SESSION = "session"
    ROLLING = "rolling"
    BACKFILL = "backfill"
    ACTIVATION_STAGE = "activation_stage"
    PARTIAL = "partial"

class DependencyClass(str, Enum):
    MUST_RUN_AFTER = "must_run_after"
    MUST_SHARE_SAME_WINDOW = "must_share_same_window"
    MUST_SHARE_SAME_SNAPSHOT = "must_share_same_snapshot"
    MUST_WAIT_FOR_GATE = "must_wait_for_gate"

class GateClass(str, Enum):
    DATA_TRUST = "data_trust"
    FEATURE_TRUST = "feature_trust"
    MODEL_TRUST = "model_trust"
    RISK = "risk"
    READINESS = "readiness"
    POLICY = "policy"
    POSITION_LEDGER_TRUTH = "position_ledger_truth"
    ACTIVATION = "activation"
    SCHEDULE_WINDOW = "schedule_window"

class RetryClass(str, Enum):
    RETRYABLE = "retryable"
    NON_RETRYABLE = "non_retryable"

class RerunClass(str, Enum):
    FULL_RERUN = "full_rerun"
    SELECTIVE_RERUN = "selective_rerun"
    SAME_WINDOW_RERUN = "same_window_rerun"

class EquivalenceVerdict(str, Enum):
    IDENTICAL = "identical"
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"
    INCOMPARABLE = "incomparable"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
