from enum import Enum

class ContinuityServiceClass(Enum):
    CRITICAL_PATH = "critical_path"
    STATE_STORE = "state_store"
    SUPPORTING_SERVICE = "supporting_service"
    ADVISORY = "advisory"

class ContinuityObjectiveClass(Enum):
    MAX_DATA_LOSS = "max_data_loss"
    TIME_TO_RECOVER = "time_to_recover"
    DEGRADED_CONTINUATION = "degraded_continuation"

class BackupClass(Enum):
    FULL = "full"
    INCREMENTAL = "incremental"
    DIFFERENTIAL = "differential"
    ADVISORY = "advisory"

class SnapshotClass(Enum):
    POINT_IN_TIME = "point_in_time"
    END_OF_DAY = "end_of_day"
    ADVISORY = "advisory"

class ReplicationClass(Enum):
    SYNC = "sync"
    ASYNC = "async"
    SEMI_SYNC = "semi_sync"

class RestoreClass(Enum):
    FULL_RESTORE = "full_restore"
    PARTIAL_RESTORE = "partial_restore"
    DRY_RUN = "dry_run"

class FailoverClass(Enum):
    PLANNED_SWITCHOVER = "planned_switchover"
    EMERGENCY_FAILOVER = "emergency_failover"
    READ_ONLY_DEGRADED = "read_only_degraded"

class FailbackClass(Enum):
    PLANNED_RETURN = "planned_return"
    EMERGENCY_RETURN = "emergency_return"

class StandbyClass(Enum):
    HOT = "hot"
    WARM = "warm"
    COLD = "cold"
    NONE = "none"

class ContinuityEquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"
    UNKNOWN = "unknown"

class ContinuityTrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
