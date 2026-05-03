from enum import Enum


class ReplayScope(str, Enum):
    TRADE = "trade"
    SESSION = "session"
    CONTROL = "control"
    GOVERNANCE = "governance"
    INCIDENT = "incident"
    RELEASE = "release"


class ReplaySourceType(str, Enum):
    PAPER_SESSION = "paper_session"
    LIVE_RUNTIME = "live_runtime"
    EXECUTION = "execution"
    APPROVAL = "approval"
    ANALYTICS = "analytics"
    INCIDENT = "incident"
    GOVERNANCE = "governance"
    QUALIFICATION = "qualification"
    RELEASE = "release"
    SECURITY = "security"


class ReplayMode(str, Enum):
    HISTORICAL = "historical"
    COUNTERFACTUAL = "counterfactual"


class CounterfactualType(str, Enum):
    ML_DISABLED = "ml_disabled"
    DIFFERENT_BUNDLE = "different_bundle"
    DIFFERENT_TRUST_VERDICT = "different_trust_verdict"
    APPROVAL_EXPIRED = "approval_expired"
    LOWER_BUDGET = "lower_budget"
    STRICTER_CONCENTRATION = "stricter_concentration"
    NO_SLIPPAGE = "no_slippage"
    HIGHER_LATENCY_CLASS = "higher_latency_class"
    CUSTOM = "custom"


class DiffSeverity(str, Enum):
    BENIGN = "benign"
    WARNING = "warning"
    CRITICAL = "critical"


class ReplayVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    UNTRUSTED = "untrusted"


class ReproducibilityStatus(str, Enum):
    EXACT_MATCH = "exact_match"
    BENIGN_MISMATCH = "benign_mismatch"
    CRITICAL_MISMATCH = "critical_mismatch"
    NON_REPRODUCIBLE = "non_reproducible"


class ForensicSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class TimelineEventType(str, Enum):
    SIGNAL = "signal"
    REGIME = "regime"
    ML_INFERENCE = "ml_inference"
    RISK_DECISION = "risk_decision"
    PORTFOLIO_DECISION = "portfolio_decision"
    CONTROL_AUTH = "control_auth"
    EXECUTION_REQUEST = "execution_request"
    EXECUTION_EVENT = "execution_event"
    ANALYTICS = "analytics"
    OBSERVABILITY = "observability"
    GOVERNANCE = "governance"
    SECURITY = "security"


class SnapshotFidelity(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    UNKNOWN = "unknown"
