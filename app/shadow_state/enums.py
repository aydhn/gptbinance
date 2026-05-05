from enum import Enum


class ShadowDomain(Enum):
    ORDERS = "orders"
    POSITIONS = "positions"
    BALANCES = "balances"
    BORROW = "borrow"
    MODES = "modes"
    COLLATERAL = "collateral"


class SnapshotSource(Enum):
    VENUE = "venue"
    LOCAL_DERIVED = "local_derived"
    TWIN = "twin"


class DriftType(Enum):
    MISSING_LOCAL = "missing_local"
    MISSING_VENUE = "missing_venue"
    VALUE_MISMATCH = "value_mismatch"
    MODE_MISMATCH = "mode_mismatch"
    STALE_DATA = "stale_data"
    UNKNOWN = "unknown"


class DriftSeverity(Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"
    BLOCKER = "blocker"


class ConvergenceVerdict(Enum):
    CLEAN = "clean"
    TRANSIENT_DIVERGENCE = "transient_divergence"
    SUSPICIOUS_DIVERGENCE = "suspicious_divergence"
    CRITICAL_DIVERGENCE = "critical_divergence"


class RemediationClass(Enum):
    NO_ACTION = "no_action"
    REVIEW_ONLY = "review_only"
    RE_FETCH = "re_fetch"
    LEDGER_INVESTIGATION = "ledger_investigation"
    LIFECYCLE_REVIEW = "lifecycle_review"
    MODE_REFRESH = "mode_refresh"
    CAPITAL_HOLD = "capital_hold"


class TruthfulnessClass(Enum):
    HIGH_CONFIDENCE = "high_confidence"
    ACCEPTABLE = "acceptable"
    DEGRADED = "degraded"
    UNTRUSTWORTHY = "untrustworthy"


class ConsistencyWindow(Enum):
    SUBMIT_ACK_TOLERANCE = "submit_ack_tolerance"
    FILL_PROPAGATION = "fill_propagation"
    CANCEL_PERSISTENCE = "cancel_persistence"
    TIMEOUT_UNKNOWN_CAUTION = "timeout_unknown_caution"
    LIVE_CAUTION_STRICT = "live_caution_strict"


class SnapshotFreshness(Enum):
    FRESH = "fresh"
    STALE = "stale"
    UNKNOWN = "unknown"


class ShadowVerdict(Enum):
    PASS = "pass"
    CAUTION = "caution"
    BLOCK = "block"
