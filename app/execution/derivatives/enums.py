from enum import Enum


class DerivativeSide(str, Enum):
    LONG = "LONG"
    SHORT = "SHORT"


class LeverageAction(str, Enum):
    INCREASE = "INCREASE"
    DECREASE = "DECREASE"
    MAINTAIN = "MAINTAIN"


class ReduceOnlyVerdict(str, Enum):
    ALLOWED = "ALLOWED"
    ADJUSTED = "ADJUSTED"
    REJECTED = "REJECTED"


class MarginCallSeverity(str, Enum):
    NORMAL = "NORMAL"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"
    LIQUIDATION_IMMINENT = "LIQUIDATION_IMMINENT"


class LiquidationProximity(str, Enum):
    SAFE = "SAFE"
    WARNING = "WARNING"
    DANGER = "DANGER"


class FundingDirection(str, Enum):
    PAY = "PAY"
    RECEIVE = "RECEIVE"


class BorrowState(str, Enum):
    HEALTHY = "HEALTHY"
    OVER_LIMIT = "OVER_LIMIT"
