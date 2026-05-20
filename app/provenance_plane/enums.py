from enum import Enum

class ProvenanceClassEnum(str, Enum):
    SOURCE = "source"
    INPUT = "input"
    TRANSFORMATION = "transformation"
    DERIVED_ARTIFACT = "derived_artifact"
    DECISION = "decision"
    ACTION = "action"
    OUTCOME = "outcome"
    ATTRIBUTION = "attribution"
    CUSTODY = "custody"
    EXPLAINABILITY = "explainability"
    RESPONSIBILITY = "responsibility"

class EquivalenceVerdictEnum(str, Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"

class TrustVerdictEnum(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
