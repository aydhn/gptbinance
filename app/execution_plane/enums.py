from enum import Enum, auto


class VenueClass(str, Enum):
    BINANCE_SPOT_MAINNET = "binance_spot_mainnet"
    BINANCE_SPOT_TESTNET = "binance_spot_testnet"
    BINANCE_FUTURES_MAINNET = "binance_futures_mainnet"
    BINANCE_FUTURES_TESTNET = "binance_futures_testnet"
    PAPER = "paper"


class ProductClass(str, Enum):
    SPOT = "spot"
    USDT_MARGINED_FUTURES = "usdt_margined_futures"
    COIN_MARGINED_FUTURES = "coin_margined_futures"


class ExecutionClass(str, Enum):
    RUNTIME = "runtime"
    PAPER = "paper"
    REPLAY = "replay"


class RoutingClass(str, Enum):
    PASSIVE = "passive"
    AGGRESSIVE = "aggressive"
    STAGED_SLICE = "staged_slice"


class OrderType(str, Enum):
    MARKET = "market"
    LIMIT = "limit"
    STOP_LOSS_LIMIT = "stop_loss_limit"
    TAKE_PROFIT_LIMIT = "take_profit_limit"
    STOP_MARKET = "stop_market"
    TAKE_PROFIT_MARKET = "take_profit_market"


class TIFClass(str, Enum):
    GTC = "gtc"
    IOC = "ioc"
    FOK = "fok"
    GTX = "gtx"  # Post-only


class FillQualityClass(str, Enum):
    PERFECT = "perfect"
    ACCEPTABLE = "acceptable"
    DEGRADED = "degraded"
    POOR = "poor"
    UNACCEPTABLE = "unacceptable"


class SlippageSeverityClass(str, Enum):
    NONE = "none"
    MILD = "mild"
    ELEVATED = "elevated"
    CRITICAL = "critical"


class EquivalenceVerdictClass(str, Enum):
    CLEAN = "clean"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"


class TrustedExecutionVerdictClass(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
