from enum import Enum


class ProductType(str, Enum):
    SPOT = "SPOT"
    MARGIN = "MARGIN"
    FUTURES_USDM = "FUTURES_USDM"
    FUTURES_COINM = "FUTURES_COINM"


class MarginMode(str, Enum):
    ISOLATED = "ISOLATED"
    CROSS = "CROSS"


class LeverageMode(str, Enum):
    FIXED = "FIXED"
    AUTO_ADJUSTED = "AUTO_ADJUSTED"


class PositionMode(str, Enum):
    ONE_WAY = "ONE_WAY"
    HEDGE = "HEDGE"


class CarryCostType(str, Enum):
    FUNDING = "FUNDING"
    BORROW_INTEREST = "BORROW_INTEREST"


class LiquidationRiskBand(str, Enum):
    SAFE = "SAFE"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"
    LIQUIDATED = "LIQUIDATED"


class ProductReadiness(str, Enum):
    DISABLED = "DISABLED"
    PAPER_ONLY = "PAPER_ONLY"
    TESTNET_ONLY = "TESTNET_ONLY"
    LIVE = "LIVE"


class SettlementType(str, Enum):
    PHYSICAL = "PHYSICAL"
    CASH = "CASH"
