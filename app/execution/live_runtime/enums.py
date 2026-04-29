from enum import Enum


class LiveRolloutMode(str, Enum):
    SHADOW_ONLY = "shadow_only"
    TESTNET_EXEC = "testnet_exec"
    CANARY_LIVE = "canary_live"
    CAPPED_LIVE = "capped_live"
    FULL_LIVE_LOCKED = "full_live_locked"


class LiveSessionStatus(str, Enum):
    INITIALIZING = "initializing"
    GATES_CHECKING = "gates_checking"
    ARMED = "armed"
    RUNNING = "running"
    FLATTENING = "flattening"
    ROLLING_BACK = "rolling_back"
    HALTED = "halted"
    COMPLETED = "completed"


class LiveRuntimeVerdict(str, Enum):
    PROCEED = "proceed"
    REJECT = "reject"
    THROTTLE = "throttle"
    HALT = "halt"


class FlattenMode(str, Enum):
    CANCEL_ONLY = "cancel_only"
    CANCEL_AND_CLOSE = "cancel_and_close"
    EMERGENCY_MARKET = "emergency_market"


class RollbackSeverity(str, Enum):
    SOFT = "soft"
    HARD = "hard"


class CapitalCapType(str, Enum):
    MAX_SESSION_NOTIONAL = "max_session_notional"
    MAX_SYMBOL_NOTIONAL = "max_symbol_notional"
    MAX_DAILY_LOSS = "max_daily_loss"
    MAX_LIVE_EXPOSURE = "max_live_exposure"
    MAX_NEW_ORDERS = "max_new_orders"


class LiveAuditEventType(str, Enum):
    SESSION_START = "session_start"
    SESSION_STOP = "session_stop"
    ORDER_SUBMIT = "order_submit"
    ORDER_REJECT = "order_reject"
    ORDER_FILL = "order_fill"
    ORDER_CANCEL = "order_cancel"
    CAPITAL_CAP_INTERVENTION = "capital_cap_intervention"
    KILL_SWITCH = "kill_switch"
    FLATTEN = "flatten"
    ROLLBACK = "rollback"
    INCIDENT_ESCALATION = "incident_escalation"


class SessionArmingStatus(str, Enum):
    DISARMED = "disarmed"
    ARMED_PENDING_GATES = "armed_pending_gates"
    ARMED_AND_VERIFIED = "armed_and_verified"


class LiveSafetyStatus(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    CRITICAL = "critical"
    HALTED = "halted"
