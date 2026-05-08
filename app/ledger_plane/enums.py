from enum import Enum

class LedgerClass(Enum):
    FILL = "fill"
    FEE = "fee"
    FUNDING = "funding"
    CARRY = "carry"
    TRANSFER = "transfer"
    MANUAL = "manual"
    COLLATERAL = "collateral"

class CashflowClass(Enum):
    TRADE = "trade"
    REALIZED_PNL = "realized_pnl"
    FEE = "fee"
    FUNDING = "funding"
    TRANSFER = "transfer"
    COLLATERAL_MOVEMENT = "collateral_movement"
    REBATE = "rebate"

class BalanceClass(Enum):
    WALLET = "wallet"
    AVAILABLE = "available"
    LOCKED = "locked"
    MARGIN = "margin"
    WITHDRAWABLE = "withdrawable"

class CollateralClass(Enum):
    USABLE = "usable"
    LOCKED = "locked"

class TransferClass(Enum):
    INTERNAL = "internal"
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"

class EquityClass(Enum):
    WALLET = "wallet"
    PNL_ADJUSTED = "pnl_adjusted"
    COLLATERAL_ADJUSTED = "collateral_adjusted"

class DivergenceSeverity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"

class AccountScopeClass(Enum):
    BINANCE_SPOT = "binance_spot"
    BINANCE_FUTURES = "binance_futures"
    PAPER = "paper"
    TESTNET = "testnet"
    SHADOW = "shadow"
