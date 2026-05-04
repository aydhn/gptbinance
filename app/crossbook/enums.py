from enum import Enum

class BookType(str, Enum):
    SPOT = "spot"
    MARGIN = "margin"
    FUTURES = "futures"

class MarginMode(str, Enum):
    CROSS = "cross"
    ISOLATED = "isolated"
    NONE = "none"

class CollateralType(str, Enum):
    USDT = "usdt"
    BUSD = "busd"
    USDC = "usdc"
    CRYPTO = "crypto"
    FIAT = "fiat"

class ExposureClass(str, Enum):
    BASE = "base"
    QUOTE = "quote"

class HedgeQuality(str, Enum):
    PERFECT = "perfect"
    GOOD = "good"
    POOR = "poor"
    FAKE = "fake"
    UNKNOWN = "unknown"

class ConflictSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class LiquidationSensitivity(str, Enum):
    SAFE = "safe"
    ELEVATED = "elevated"
    DANGER = "danger"

class FundingBurdenClass(str, Enum):
    NEGLIGIBLE = "negligible"
    NOTICEABLE = "noticeable"
    DRAG = "drag"
    UNACCEPTABLE = "unacceptable"

class BorrowDependencyClass(str, Enum):
    NONE = "none"
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"

class CrossBookVerdict(str, Enum):
    ALLOW = "allow"
    CAUTION = "caution"
    REDUCE = "reduce"
    DEFER = "defer"
    BLOCK = "block"
    HEDGE_QUALITY_WARNING = "hedge_quality_warning"
    COLLATERAL_WARNING = "collateral_warning"
    FUNDING_DRAG_WARNING = "funding_drag_warning"
    LIQUIDATION_WARNING = "liquidation_warning"
