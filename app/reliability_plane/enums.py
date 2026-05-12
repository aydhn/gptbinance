from enum import Enum


class ReliabilityServiceClass(str, Enum):
    EXECUTION = "execution"
    RISK = "risk"
    RELEASE = "release"
    WORKFLOW = "workflow"
    DATA = "data"
    MODEL = "model"
    LEDGER = "ledger"
    OBSERVABILITY = "observability"
    CONTROL = "control"
    OTHER = "other"


class ReliabilityObjectiveClass(str, Enum):
    AVAILABILITY = "availability"
    CORRECTNESS = "correctness"
    LATENCY = "latency"
    FRESHNESS = "freshness"
    RECOVERABILITY = "recoverability"
    CONTINUITY = "continuity"


class SLIClass(str, Enum):
    SUCCESS_RATE = "success_rate"
    LATENCY_PERCENTILE = "latency_percentile"
    FRESHNESS_LAG = "freshness_lag"
    DATA_CORRECTNESS = "data_correctness"
    RECOVERY_TIME = "recovery_time"
    CONTINUITY_COVERAGE = "continuity_coverage"


class SLOClass(str, Enum):
    HARD = "hard"
    ADVISORY = "advisory"


class BudgetClass(str, Enum):
    STRICT = "strict"
    FLEXIBLE = "flexible"


class BurnRateClass(str, Enum):
    NOMINAL = "nominal"
    ELEVATED = "elevated"
    CRITICAL = "critical"
    EXHAUSTED = "exhausted"


class MaintenanceClass(str, Enum):
    PLANNED = "planned"
    EMERGENCY = "emergency"


class DegradedModeClass(str, Enum):
    PARTIAL_SERVICE = "partial_service"
    CANARY_ONLY = "canary_only"
    NO_NEW_EXPOSURE = "no_new_exposure"
    READ_ONLY = "read_only"


class ReliabilityStateClass(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    MAINTENANCE = "maintenance"
    BUDGET_EXHAUSTED = "budget_exhausted"
    RECOVERING = "recovering"
    STABILIZED = "stabilized"
    UNKNOWN = "unknown"


class ReliabilityEquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"
    UNKNOWN = "unknown"


class ReliabilityTrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
