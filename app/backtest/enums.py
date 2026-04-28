from enum import Enum, auto


class BacktestMode(Enum):
    STANDARD = auto()
    WALK_FORWARD = auto()  # Placeholder for future


class OrderSide(Enum):
    BUY = auto()
    SELL = auto()


class FillAssumption(Enum):
    NEXT_BAR_OPEN = auto()
    SAME_BAR_CLOSE = auto()
    WORST_CASE = auto()


class PositionSide(Enum):
    LONG = auto()
    SHORT = auto()
    FLAT = auto()


class TradeStatus(Enum):
    OPEN = auto()
    CLOSED = auto()


class CostModelType(Enum):
    ZERO_FEE = auto()
    FIXED_BPS = auto()
    TIERED = auto()


class SlippageModelType(Enum):
    ZERO_SLIPPAGE = auto()
    FIXED_BPS = auto()
    VOLATILITY_SCALED = auto()


class SignalHandlingMode(Enum):
    IGNORE_IF_IN_POSITION = auto()
    REVERSE_ALLOWED = auto()
    SCALE_IN_ALLOWED = auto()


class ExposureMode(Enum):
    SINGLE_POSITION = auto()  # Max 1 active position at a time
    PORTFOLIO = auto()  # Multiple concurrent positions
