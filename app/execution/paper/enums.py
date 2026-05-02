"""Enums for paper trading runtime."""

from enum import Enum, auto


class PaperOrderStatus(str, Enum):
    CREATED = "created"
    QUEUED = "queued"
    ACCEPTED = "accepted"
    PARTIALLY_FILLED = "partially_filled"
    FILLED = "filled"
    CANCELLED = "cancelled"
    REJECTED = "rejected"
    EXPIRED = "expired"


class PaperSessionStatus(str, Enum):
    INITIALIZED = "initialized"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"


class PaperEventType(str, Enum):
    ORDER_CREATED = "order_created"
    ORDER_ACCEPTED = "order_accepted"
    ORDER_FILLED = "order_filled"
    ORDER_REJECTED = "order_rejected"
    ORDER_CANCELLED = "order_cancelled"
    POSITION_OPENED = "position_opened"
    POSITION_CLOSED = "position_closed"
    POSITION_REDUCED = "position_reduced"
    POSITION_REVERSED = "position_reversed"
    PNL_UPDATED = "pnl_updated"
    HEALTH_DEGRADED = "health_degraded"
    KILL_SWITCH_TRIGGERED = "kill_switch_triggered"
    SESSION_STARTED = "session_started"
    SESSION_STOPPED = "session_stopped"


class FillTrigger(str, Enum):
    NEXT_TICK = "next_tick"
    NEXT_BAR = "next_bar"
    IMMEDIATE = "immediate"  # Not recommended for realism


class SessionStopReason(str, Enum):
    MANUAL = "manual"
    DURATION_REACHED = "duration_reached"
    KILL_SWITCH = "kill_switch"
    ERROR = "error"


class PnlMode(str, Enum):
    MARK_TO_MARKET = "mark_to_market"


class RuntimeDecisionStatus(str, Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    VETOED_BY_RISK = "vetoed_by_risk"


class SessionHealth(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    CRITICAL = "critical"
    HALTED = "halted"
