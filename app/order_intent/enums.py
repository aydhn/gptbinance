from enum import Enum


class IntentType(str, Enum):
    OPEN_LONG = "open_long"
    OPEN_SHORT = "open_short"
    OPEN_SMALL_PROBE = "open_small_probe"
    SCALE_IN_EXISTING = "scale_in_existing"
    REDUCE_POSITION = "reduce_position"
    CLOSE_POSITION = "close_position"
    FLATTEN_SYMBOL = "flatten_symbol"
    EXIT_ONLY_FLATTEN = "exit_only_flatten"
    ROTATE_EXPOSURE = "rotate_exposure"
    DE_RISK_POSITION = "de_risk_position"
    REDUCE_CLUSTER_EXPOSURE = "reduce_cluster_exposure"
    REDUCE_DUE_TO_EVENT_RISK = "reduce_due_to_event_risk"
    MARGIN_BORROW_BACKED_BUY = "margin_borrow_backed_buy"
    MARGIN_REPAY_AFTER_REDUCE = "margin_repay_after_reduce"
    FUTURES_REDUCE_ONLY_CLOSE = "futures_reduce_only_close"
    FUTURES_CLOSE_POSITION_ALL = "futures_close_position_all"


class PlanType(str, Enum):
    SINGLE_LEG = "single_leg"
    MULTI_LEG = "multi_leg"


class OrderLegType(str, Enum):
    SPOT_TRADE = "spot_trade"
    MARGIN_TRADE = "margin_trade"
    FUTURES_TRADE = "futures_trade"
    MARGIN_BORROW = "margin_borrow"
    MARGIN_REPAY = "margin_repay"


class VenueProduct(str, Enum):
    SPOT = "spot"
    MARGIN_CROSS = "margin_cross"
    MARGIN_ISOLATED = "margin_isolated"
    FUTURES_USDM = "futures_usdm"
    FUTURES_COINM = "futures_coinm"


class AccountMode(str, Enum):
    SPOT_ONLY = "spot_only"
    CROSS_MARGIN_ENABLED = "cross_margin_enabled"
    ISOLATED_MARGIN_ONLY = "isolated_margin_only"
    FUTURES_ONE_WAY = "futures_one_way"
    FUTURES_HEDGE_MODE = "futures_hedge_mode"


class PositionMode(str, Enum):
    ONE_WAY = "one_way"
    HEDGE = "hedge"


class CompileVerdict(str, Enum):
    SUCCESS = "success"
    CAUTION = "caution"
    BLOCKED = "blocked"
    FAILED = "failed"


class SemanticSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class BorrowMode(str, Enum):
    AUTO_BORROW = "auto_borrow"
    EXPLICIT_BORROW = "explicit_borrow"
    NO_BORROW = "no_borrow"


class SafetyMode(str, Enum):
    STRICT = "strict"
    FLEXIBLE = "flexible"


class OrderSide(str, Enum):
    BUY = "buy"
    SELL = "sell"


class PositionSide(str, Enum):
    LONG = "long"
    SHORT = "short"
    BOTH = "both"
