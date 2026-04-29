from enum import Enum


class OpsMode(str, Enum):
    DEV = "dev"
    PAPER = "paper"
    TESTNET = "testnet"
    LIVE = "live"


class RolloutMode(str, Enum):
    STANDARD = "standard"
    SHADOW = "shadow"
    CANARY = "canary"


class ReadinessVerdict(str, Enum):
    PASS = "pass"
    CAUTION = "caution"
    FAIL = "fail"


class IncidentType(str, Enum):
    STREAM_DEGRADED = "stream_degraded"
    EXECUTION_REJECT_STORM = "execution_reject_storm"
    RECONCILIATION_DRIFT = "reconciliation_drift"
    DRAWDOWN_HARD_STOP = "drawdown_hard_stop"
    NOTIFIER_FAIL = "notifier_fail"
    STORAGE_CORRUPTION = "storage_corruption"
    REPEATED_RUNTIME_CRASH = "repeated_runtime_crash"
    UNKNOWN_ORDER_STATE = "unknown_order_state"
    CONFIG_MISMATCH = "config_mismatch"
    KILL_SWITCH_ACTIVE = "kill_switch_active"
    LIVE_REJECT_STORM = "live_reject_storm"
    LIVE_FILL_MISMATCH = "live_fill_mismatch"
    CAPITAL_CAP_BREACH = "capital_cap_breach"
    FLATTEN_INCOMPLETE = "flatten_incomplete"
    ROLLBACK_INCOMPLETE = "rollback_incomplete"


class IncidentSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class MaintenanceStatus(str, Enum):
    SCHEDULED = "scheduled"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class SupervisorStatus(str, Enum):
    INITIALIZING = "initializing"
    READY = "ready"
    STARTING = "starting"
    RUNNING = "running"
    PAUSED = "paused"
    DRAINING = "draining"
    STOPPING = "stopping"
    STOPPED = "stopped"
    HALTED_ON_ERROR = "halted_on_error"


class ControlAction(str, Enum):
    START = "start"
    PAUSE = "pause"
    RESUME = "resume"
    DRAIN = "drain"
    STOP = "stop"
    FORCE_HALT = "force_halt"


class RecoveryVerdict(str, Enum):
    RECOVERABLE = "recoverable"
    CAUTION = "caution"
    HALT = "halt"


class GoLiveVerdict(str, Enum):
    PASS = "pass"
    CAUTION = "caution"
    FAIL = "fail"
