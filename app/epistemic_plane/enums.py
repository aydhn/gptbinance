from enum import Enum

class EpistemicClass(str, Enum):
    FACT = "fact"
    CLAIM = "claim"
    INFERENCE = "inference"
    HYPOTHESIS = "hypothesis"
    ASSUMPTION = "assumption"
    ESTIMATE = "estimate"
    UNKNOWN = "unknown"
    REFUTATION = "refutation"
    CONTRADICTION = "contradiction"

class EvidenceClass(str, Enum):
    DIRECT = "direct"
    INDIRECT = "indirect"
    CORROBORATING = "corroborating"
    CONFLICTING = "conflicting"

class SufficiencyClass(str, Enum):
    INSUFFICIENT = "insufficient"
    MINIMALLY_SUFFICIENT = "minimally_sufficient"
    STRONG_ENOUGH = "strong_enough"
    DEGRADED = "degraded"

class ConfidenceClass(str, Enum):
    OBSERVATIONAL = "observational"
    INFERENTIAL = "inferential"
    DECISION = "decision"
    CALIBRATED = "calibrated"

class UncertaintyClass(str, Enum):
    DATA = "data"
    MODEL = "model"
    SEMANTIC = "semantic"
    TEMPORAL = "temporal"
    UNKNOWN_UNKNOWN = "unknown_unknown"

class KnowabilityClass(str, Enum):
    KNOWABLE_WITH_CURRENT_EVIDENCE = "knowable_with_current_evidence"
    KNOWABLE_WITH_MORE_EVIDENCE = "knowable_with_more_evidence"
    PRACTICALLY_UNKNOWABLE = "practically_unknowable"
    BOUNDED_UNKNOWABILITY = "bounded_unknowability"

class ContradictionClass(str, Enum):
    DIRECT = "direct"
    LATENT = "latent"
    CROSS_PLANE = "cross_plane"

class RefutationClass(str, Enum):
    PARTIAL = "partial"
    FULL = "full"

class EpistemicTrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"

class EpistemicEquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"
