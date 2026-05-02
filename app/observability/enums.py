from enum import Enum


class MetricType(str, Enum):
    COUNTER = "counter"
    GAUGE = "gauge"
    HISTOGRAM = "histogram"
    EVENT = "event"


class MetricUnit(str, Enum):
    COUNT = "count"
    SECONDS = "seconds"
    MILLISECONDS = "milliseconds"
    PERCENTAGE = "percentage"
    BYTES = "bytes"
    CURRENCY = "currency"
    NONE = "none"


class ComponentType(str, Enum):
    DATA_STREAM = "data_stream"
    EXECUTION = "execution"
    RISK_ENGINE = "risk_engine"
    PORTFOLIO = "portfolio"
    STRATEGY = "strategy"
    SUPERVISOR = "supervisor"
    GOVERNANCE = "governance"
    SECURITY = "security"
    AUTOMATION = "automation"
    SYSTEM = "system"


class HealthSeverity(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    CRITICAL = "critical"
    HALTED = "halted"


class AlertSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class AlertState(str, Enum):
    OPEN = "open"
    ACKNOWLEDGED = "acknowledged"
    SUPPRESSED = "suppressed"
    CLEARED = "cleared"


class CorrelationVerdict(str, Enum):
    UNRELATED = "unrelated"
    RELATED = "related"
    SAME_ROOT_CAUSE = "same_root_cause"


class SloStatus(str, Enum):
    HEALTHY = "healthy"
    CAUTION = "caution"
    BREACH = "breach"


class DigestScope(str, Enum):
    SESSION = "session"
    DAILY = "daily"
    WEEKLY = "weekly"


class SuppressionAction(str, Enum):
    ALLOW = "allow"
    SUPPRESS = "suppress"
    DELAY = "delay"
