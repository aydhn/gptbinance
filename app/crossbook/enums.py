"""
enums.py
"""
from enum import Enum


class BookType(Enum):
    SPOT = "SPOT"
    MARGIN = "MARGIN"
    FUTURES = "FUTURES"


class MarginMode(Enum):
    ISOLATED = "ISOLATED"
    CROSS = "CROSS"
    NONE = "NONE"


class CollateralType(Enum):
    CASH = "CASH"
    CRYPTO_BASE = "CRYPTO_BASE"
    CRYPTO_QUOTE = "CRYPTO_QUOTE"


class ExposureClass(Enum):
    DIRECTIONAL_LONG = "DIRECTIONAL_LONG"
    DIRECTIONAL_SHORT = "DIRECTIONAL_SHORT"
    NEUTRAL_HEDGED = "NEUTRAL_HEDGED"
    FAKE_HEDGED = "FAKE_HEDGED"


class HedgeQuality(Enum):
    PERFECT = "PERFECT"
    ACCEPTABLE = "ACCEPTABLE"
    POOR = "POOR"
    FAKE = "FAKE"


class ConflictSeverity(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class LiquidationSensitivity(Enum):
    SAFE = "SAFE"
    ELEVATED = "ELEVATED"
    DANGEROUS = "DANGEROUS"


class FundingBurdenClass(Enum):
    NEGLIGIBLE = "NEGLIGIBLE"
    NOTICEABLE = "NOTICEABLE"
    SEVERE = "SEVERE"


class BorrowDependencyClass(Enum):
    NONE = "NONE"
    MODERATE = "MODERATE"
    HIGH = "HIGH"


class CrossBookVerdict(Enum):
    ALLOW = "ALLOW"
    CAUTION = "CAUTION"
    REDUCE = "REDUCE"
    DEFER = "DEFER"
    BLOCK = "BLOCK"


class OverlayReasonType(Enum):
    FAKE_HEDGE_DETECTED = "FAKE_HEDGE_DETECTED"
    COLLATERAL_PRESSURE_HIGH = "COLLATERAL_PRESSURE_HIGH"
    BORROW_DEPENDENCY_ELEVATED = "BORROW_DEPENDENCY_ELEVATED"
    COMBINED_EXPOSURE_BREACH = "COMBINED_EXPOSURE_BREACH"
    FUNDING_BURDEN_CAUTION = "FUNDING_BURDEN_CAUTION"
    LEVERAGE_STACKING = "LEVERAGE_STACKING"
