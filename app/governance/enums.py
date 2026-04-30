from enum import Enum


class RefreshTriggerType(str, Enum):
    TIME_BASED = "time_based"
    NEW_DATA = "new_data"
    DRIFT_DECAY = "drift_decay"
    MANUAL = "manual"
    FAILED_RETRY = "failed_retry"


class BundleType(str, Enum):
    STRATEGY = "strategy"
    ML = "ml"
    FULL = "full"


class BundleStage(str, Enum):
    CANDIDATE = "candidate"
    REVIEWED = "reviewed"
    APPROVED_FOR_SHADOW = "approved_for_shadow"
    APPROVED_FOR_PAPER = "approved_for_paper"
    APPROVED_FOR_TESTNET_EXEC = "approved_for_testnet_exec"
    APPROVED_FOR_LIVE_CAUTION = "approved_for_live_caution"
    ACTIVE = "active"
    RETIRED = "retired"
    REJECTED = "rejected"


class PromotionReadiness(str, Enum):
    READY = "ready"
    CAUTION = "caution"
    BLOCKED = "blocked"


class DecaySeverity(str, Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class DegradationType(str, Enum):
    OOS_DECAY = "oos_decay"
    LIVE_PAPER_DIVERGENCE = "live_paper_divergence"
    CALIBRATION_DECAY = "calibration_decay"
    DRIFT = "drift"
    HIT_RATE_COLLAPSE = "hit_rate_collapse"


class RollbackStatus(str, Enum):
    READY = "ready"
    MISSING_REFERENCE = "missing_reference"
    UNSAFE = "unsafe"


class GovernanceVerdict(str, Enum):
    PASS = "pass"
    CAUTION = "caution"
    FAIL = "fail"


class ActivationMode(str, Enum):
    SHADOW = "shadow"
    PAPER = "paper"
    TESTNET = "testnet"
    LIVE_CAUTION = "live_caution"
