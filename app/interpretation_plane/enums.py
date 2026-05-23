from enum import Enum, auto

class InterpretationClass(Enum):
    CONTRACT_CLAUSE = auto()
    POLICY_RULE = auto()
    REPRESENTATION_TEXT = auto()
    RIGHTS_TEXT = auto()
    LIABILITY_CLAUSE = auto()
    FINALITY_LABEL = auto()
    COMMITMENT_LANGUAGE = auto()
    COMPLIANCE_TERM = auto()
    SECURITY_STATUS = auto()
    AUTONOMY_EXPLANATION = auto()
    FEDERATED_TRANSLATION = auto()
    CROSS_PLANE_CANONICAL = auto()

class TextUnitClass(Enum):
    DOCUMENT = auto()
    CLAUSE = auto()
    SENTENCE = auto()
    PHRASE = auto()
    TERM = auto()

class ReadingClass(Enum):
    TEXTUAL = auto()
    CONTEXTUAL = auto()
    PURPOSIVE = auto()
    RESTRICTIVE = auto()
    EXPANSIVE = auto()

class AmbiguityClass(Enum):
    TEXTUAL = auto()
    SCOPE = auto()
    TEMPORAL = auto()
    BENEFICIARY = auto()

class ClarificationClass(Enum):
    WORDING = auto()
    SCOPE = auto()
    AUDIENCE = auto()
    INSUFFICIENT = auto()

class ConflictClass(Enum):
    TEXT_VS_CONTEXT = auto()
    CONTEXT_VS_PURPOSE = auto()
    LOCAL_VS_GLOBAL = auto()
    BENEFICIARY_VS_LIMITER = auto()

class HierarchyClass(Enum):
    CONSTITUTIONAL = auto()
    CONTRACTUAL = auto()
    AUTHORITATIVE = auto()
    ADVISORY = auto()
    LOCAL = auto()

class ScopeClass(Enum):
    TERM = auto()
    CLAUSE = auto()
    DOCUMENT = auto()
    CROSS_PLANE = auto()

class DriftClass(Enum):
    WORDING = auto()
    MEANING = auto()
    USAGE = auto()
    DEPRECATED_READING = auto()

class EquivalenceVerdict(Enum):
    EQUIVALENT = auto()
    PARTIAL = auto()
    DIVERGENT = auto()
    ORPHANED = auto()

class InterpretationTrustVerdict(Enum):
    TRUSTED = auto()
    CAUTION = auto()
    DEGRADED = auto()
    BLOCKED = auto()
    REVIEW_REQUIRED = auto()
