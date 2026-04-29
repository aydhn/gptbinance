from enum import Enum, auto


class RiskVerdict(Enum):
    APPROVE = auto()
    REDUCE = auto()
    DEFER = auto()
    REJECT = auto()


class VetoSeverity(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


class ThrottleType(Enum):
    NONE = auto()
    SYMBOL_COOLDOWN = auto()
    STRATEGY_COOLDOWN = auto()
    DRAWDOWN_SLOWDOWN = auto()
    REGIME_THROTTLE = auto()


class SizingMode(Enum):
    FIXED_FRACTION = auto()
    VOLATILITY_ADJUSTED = auto()
    FIXED_NOTIONAL = auto()


class ExposureScope(Enum):
    ACCOUNT = auto()
    STRATEGY = auto()
    SYMBOL = auto()
    DIRECTION = auto()


class RiskEventType(Enum):
    POLICY_VIOLATION = auto()
    DRAWDOWN_THRESHOLD = auto()
    KILL_SWITCH_ACTIVATED = auto()
    KILL_SWITCH_DEACTIVATED = auto()
    CAP_REACHED = auto()


class KillSwitchType(Enum):
    DRAWDOWN_BREACH = auto()
    EXPOSURE_EXPLOSION = auto()
    DATA_STALE = auto()
    REJECT_STORM = auto()
    MANUAL = auto()
    CONFIG_CORRUPTION = auto()


class DrawdownState(Enum):
    NORMAL = auto()
    CAUTION = auto()
    REDUCE = auto()
    HARD_STOP = auto()


class ApprovalStatus(Enum):
    APPROVED = auto()
    REJECTED = auto()


class RegimeRiskMode(Enum):
    NORMAL = auto()
    CAUTION = auto()
    RESTRICTIVE = auto()
