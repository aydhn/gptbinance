from enum import Enum

class TemporalClass(Enum):
    EVENT = "event"
    PROCESSING = "processing"
    DECISION = "decision"
    APPROVAL = "approval"
    EXECUTION = "execution"
    EFFECT = "effect"
    OBSERVATION = "observation"

class ClockClass(Enum):
    SOURCE = "source"
    SYSTEM = "system"
    VENDOR = "vendor"
    FEDERATED = "federated"

class TimestampClass(Enum):
    SIGNED = "signed"
    OBSERVED = "observed"
    INFERRED = "inferred"
    BACKFILLED = "backfilled"

class WindowClass(Enum):
    VALIDITY = "validity"
    EXECUTION = "execution"
    OBSERVATION = "observation"
    VERIFICATION = "verification"
    CONSTITUTIONAL = "constitutional"

class FreshnessClass(Enum):
    FRESH = "fresh"
    FRESH_ENOUGH = "fresh_enough"
    AGING = "aging"
    UNKNOWN = "unknown"
    STALE = "stale"

class StalenessClass(Enum):
    NOT_STALE = "not_stale"
    STALE_EVIDENCE = "stale_evidence"
    STALE_APPROVAL = "stale_approval"
    STALE_CONFIG = "stale_config"
    STALE_OBSERVATION = "stale_observation"

class DeadlineClass(Enum):
    HARD = "hard"
    SOFT = "soft"
    LEGAL = "legal"
    OPERATOR = "operator"

class OrderingClass(Enum):
    SOURCE = "source"
    PROCESSING = "processing"
    CAUSAL = "causal"
    RECONSTRUCTED = "reconstructed"
    AMBIGUOUS = "ambiguous"

class AdmissibilityClass(Enum):
    ADMISSIBLE = "admissible"
    DEGRADED = "degraded"
    INADMISSIBLE = "inadmissible"

class CausalityClass(Enum):
    BEFORE = "before"
    AFTER = "after"
    CONCURRENT = "concurrent"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"
    UNVERIFIABLE = "unverifiable"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
