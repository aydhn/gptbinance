from enum import Enum


class ScenarioType(str, Enum):
    PRICE_GAP = "PRICE_GAP"
    LIQUIDITY_SHOCK = "LIQUIDITY_SHOCK"
    CORRELATION_SPIKE = "CORRELATION_SPIKE"
    FUNDING_SPIKE = "FUNDING_SPIKE"
    EVENT_CLUSTER = "EVENT_CLUSTER"
    DERIVATIVES_SHOCK = "DERIVATIVES_SHOCK"
    COMPOSITE = "COMPOSITE"


class ShockType(str, Enum):
    PRICE = "PRICE"
    VOLATILITY = "VOLATILITY"
    SPREAD = "SPREAD"
    SLIPPAGE = "SLIPPAGE"
    LIQUIDITY = "LIQUIDITY"
    CORRELATION = "CORRELATION"
    FUNDING = "FUNDING"
    BORROW = "BORROW"
    LATENCY = "LATENCY"


class LossSeverity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"
    CATASTROPHIC = "CATASTROPHIC"


class BudgetVerdict(str, Enum):
    PASS = "PASS"
    CAUTION = "CAUTION"
    BREACH = "BREACH"


class StressOverlayVerdict(str, Enum):
    ALLOW = "ALLOW"
    CAUTION = "CAUTION"
    REDUCE = "REDUCE"
    DEFER = "DEFER"
    BLOCK = "BLOCK"
    EXIT_ONLY_ADVISORY = "EXIT_ONLY_ADVISORY"


class VulnerabilityType(str, Enum):
    CONCENTRATION = "CONCENTRATION"
    ILLIQUIDITY = "ILLIQUIDITY"
    CROSS_MARGIN = "CROSS_MARGIN"
    HIGH_CORRELATION = "HIGH_CORRELATION"
    FUNDING_BURDEN = "FUNDING_BURDEN"


class StressSource(str, Enum):
    HISTORICAL = "HISTORICAL"
    HYPOTHETICAL = "HYPOTHETICAL"
    EVENT_DRIVEN = "EVENT_DRIVEN"


class ScenarioConfidence(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class TailRiskClass(str, Enum):
    TAIL_95 = "TAIL_95"
    TAIL_99 = "TAIL_99"
    TAIL_99_9 = "TAIL_99_9"


class StressVerdict(str, Enum):
    SAFE = "SAFE"
    VULNERABLE = "VULNERABLE"
    DANGEROUS = "DANGEROUS"
