from enum import Enum


class AnalyticsScope(Enum):
    SESSION = "session"
    DAILY = "daily"
    WEEKLY = "weekly"
    ALL = "all"


class AttributionType(Enum):
    STRATEGY = "strategy"
    REGIME = "regime"
    PORTFOLIO = "portfolio"


class DivergenceType(Enum):
    BACKTEST_VS_PAPER = "backtest_vs_paper"
    PAPER_VS_LIVE = "paper_vs_live"
    DECISION_VS_EXECUTION = "decision_vs_execution"


class AnomalySeverity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ExecutionQualityVerdict(Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    DEGRADED = "degraded"
    POOR = "poor"
    UNACCEPTABLE = "unacceptable"


class JournalEventType(Enum):
    SIGNAL_GENERATED = "signal_generated"
    RISK_EVALUATED = "risk_evaluated"
    PORTFOLIO_ALLOCATED = "portfolio_allocated"
    ORDER_SUBMITTED = "order_submitted"
    ORDER_FILLED = "order_filled"
    ORDER_REJECTED = "order_rejected"
    ORDER_CANCELLED = "order_cancelled"
    POSITION_CLOSED = "position_closed"


class ComparisonVerdict(Enum):
    MATCH = "match"
    MINOR_DIVERGENCE = "minor_divergence"
    MAJOR_DIVERGENCE = "major_divergence"
    CRITICAL_DIVERGENCE = "critical_divergence"


class DiagnosticConfidence(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CERTAIN = "certain"


class PeriodGranularity(Enum):
    SESSION = "session"
    DAY = "day"
    WEEK = "week"
