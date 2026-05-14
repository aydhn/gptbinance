from enum import Enum


class ResourceClass(str, Enum):
    COMPUTE = "compute"
    GPU = "gpu"
    MEMORY = "memory"
    STORAGE_IOPS = "storage_iops"
    STORAGE_BYTES = "storage_bytes"
    NETWORK_BANDWIDTH = "network_bandwidth"
    QUEUE_LANE = "queue_lane"
    MODEL_SERVING_SLOT = "model_serving_slot"
    CONCURRENCY_SLOT = "concurrency_slot"
    EXTERNAL_API_QUOTA = "external_api_quota"
    EXCHANGE_RATE_LIMIT = "exchange_rate_limit"
    UNKNOWN = "unknown"


class QuotaClass(str, Enum):
    HARD = "hard"
    SOFT = "soft"
    BURST = "burst"
    TIME_WINDOW = "time_window"
    VENDOR_DEFINED = "vendor_defined"
    UNKNOWN = "unknown"


class WorkloadClass(str, Enum):
    LIVE_TRADING = "live_trading"
    PROBATION = "probation"
    PAPER = "paper"
    REPLAY = "replay"
    RESEARCH = "research"
    EXPERIMENT = "experiment"
    BACKFILL = "backfill"
    EMERGENCY_RECOVERY = "emergency_recovery"
    SYSTEM_CONTROL = "system_control"
    UNKNOWN = "unknown"


class PriorityClass(str, Enum):
    EMERGENCY_OVERRIDE = "emergency_override"
    CRITICAL = "critical"
    HIGH = "high"
    NORMAL = "normal"
    BEST_EFFORT = "best_effort"
    BACKGROUND = "background"
    UNKNOWN = "unknown"


class ReservationClass(str, Enum):
    GUARANTEED = "guaranteed"
    SOFT_RESERVED = "soft_reserved"
    TIME_BOUNDED = "time_bounded"
    ENVIRONMENT_BOUND = "environment_bound"
    UNKNOWN = "unknown"


class SaturationSeverity(str, Enum):
    NORMAL = "normal"
    WARNING = "warning"
    CRITICAL = "critical"
    EXHAUSTED = "exhausted"
    UNKNOWN = "unknown"


class ThrottlingClass(str, Enum):
    GRACEFUL = "graceful"
    HARD_BLOCK = "hard_block"
    DELAYED = "delayed"
    UNKNOWN = "unknown"


class SheddingClass(str, Enum):
    LOW_PRIORITY_DROP = "low_priority_drop"
    NO_NEW_EXPOSURE = "no_new_exposure"
    DEGRADED_READ_ONLY = "degraded_read_only"
    TOTAL_SHED = "total_shed"
    UNKNOWN = "unknown"


class FairnessClass(str, Enum):
    EQUITABLE = "equitable"
    DOMINATED = "dominated"
    STARVED = "starved"
    UNKNOWN = "unknown"


class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"
    UNKNOWN = "unknown"


class CapacityTrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
    UNKNOWN = "unknown"
