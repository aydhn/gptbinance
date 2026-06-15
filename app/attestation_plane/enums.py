from enum import Enum

class AttestationClass(Enum):
    STANDARD = "standard"
    PROVISIONAL = "provisional"

class ClaimClass(Enum):
    CLEAN_STATE = "clean_state"
    CONDITIONAL = "conditional"

class BasisClass(Enum):
    SUFFICIENT = "sufficient"
    PARTIAL = "partial"

class AttestorClass(Enum):
    INTERNAL = "internal"
    EXTERNAL = "external"

class ScopeClass(Enum):
    BOUNDED = "bounded"
    BROAD = "broad"

class ValidityClass(Enum):
    BOUNDED = "bounded"
    OVERLONG = "overlong"

class ContradictionClass(Enum):
    DIRECT = "direct"
    TEMPORAL = "temporal"

class RevocationClass(Enum):
    VALID = "valid"
    PARTIAL = "partial"

class DebtClass(Enum):
    STALE_CITATION = "stale_citation"
    SCOPE_LAUNDERING = "scope_laundering"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
