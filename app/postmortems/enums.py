from enum import Enum


class PostmortemClass(str, Enum):
    INCIDENT_LEARNING = "incident_learning"
    NEAR_MISS = "near_miss"
    OPERATIONAL_DRIFT = "operational_drift"


class EvidenceVerdict(str, Enum):
    ACCEPTED = "accepted"
    CAUTION = "caution"
    INADMISSIBLE = "inadmissible"


class ChronologyConfidence(str, Enum):
    VERIFIED = "verified"
    PARTIALLY_VERIFIED = "partially_verified"
    UNCERTAIN = "uncertain"


class CausalFactorClass(str, Enum):
    ROOT_CAUSE = "root_cause"
    CONTRIBUTING_FACTOR = "contributing_factor"
    TRIGGER = "trigger"


class RootCauseConfidence(str, Enum):
    CONFIRMED = "confirmed"
    LIKELY = "likely"
    SPECULATIVE = "speculative"
    UNRESOLVED = "unresolved"


class ActionClass(str, Enum):
    CORRECTIVE = "corrective"
    PREVENTIVE = "preventive"
    DOCUMENTATION = "documentation"
    POLICY_GAP = "policy_gap"


class RecurrenceClass(str, Enum):
    HIGH_RISK = "high_risk"
    MEDIUM_RISK = "medium_risk"
    LOW_RISK = "low_risk"


class LearningDebtSeverity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class PostmortemState(str, Enum):
    DRAFT = "draft"
    EVIDENCE_GATHERING = "evidence_gathering"
    ANALYSIS = "analysis"
    FINALIZED = "finalized"
    CLOSED = "closed"


class PostmortemVerdictClass(str, Enum):
    CONCLUSIVE = "conclusive"
    WEAK = "weak"
    INCONCLUSIVE = "inconclusive"
